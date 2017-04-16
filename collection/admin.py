from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse

import tempfile
import zipfile
import json
import pandas as pd
from pandas.io.json import json_normalize
import datetime
import csv
from django.utils.encoding import smart_str

# Register your models here.
from .models import Questionnaire, ExperimentPage, Questions, Sequences

def export_questionaire(modeladmin, request, queryset):
    files = []
    participants = []
    for obj in queryset:
        try:
            participants.append(obj)
            df = pd.concat(participants, ignore_index=True)

            df.to_csv('{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M')))
            files.append('{}_{}.csv'.format(obj.pid, obj.question_number))
            
            with tempfile.SpooledTemporaryFile() as tmp:
                with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as archive:
                    for file in files:
                        archive.write(file)
                # Reset file pointer
                tmp.seek(0)
                # Write file data to response
                response = HttpResponse(tmp.read(), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename={}.zip'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M'))
                return response
        except:
            print('Error')

def export_csv(modeladmin, request, queryset):

    files = []
    
    # Open an error file
    with open('error_{}.txt'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M')), 'w') as f:
        for obj in queryset:
            try:
                gaze = json.loads(obj.gazedata)
                frames = []
                for item in gaze:
                    frames.append(json_normalize(json.loads(item)))

                df = pd.concat(frames, ignore_index=True)
                df.set_index('time', inplace=True)

                df.to_csv('{}_{}.csv'.format(obj.pid, obj.question_number))
                files.append('{}_{}.csv'.format(obj.pid, obj.question_number))
            except:
                f.write('No gaze data for participant {} question number {}. \r\n'.format(obj.pid, obj.question_number))
        
        files.append('error_{}.txt'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M')))
    
    with tempfile.SpooledTemporaryFile() as tmp:
        with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as archive:
            for file in files:
                archive.write(file)
        # Reset file pointer
        tmp.seek(0)
        # Write file data to response
        response = HttpResponse(tmp.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename={}.zip'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M'))
        return response

export_csv.short_description = u"Export CSV"

# for importing and exporting the questions data
class QuestionsResource(resources.ModelResource):
    class Meta:
        model = Questions

class QuestionsAdmin(ImportExportModelAdmin):
    resource_class = QuestionsResource
    list_display = ('id','question_text','question_number', 'image_ref')
    readonly_fields = ('id','question_text','answer', 'question_number', 'image_ref')

# for importing and exporting the questionnaire data
class QuestionnaireResource(resources.ModelResource):
    class Meta:
        model = Questionnaire

class QuestionnaireAdmin(ImportExportModelAdmin):
    resource_class = QuestionnaireResource
    list_display = ('id','timestamp')
    readonly_fields = ('id','timestamp', 'age', 'gender', 'education', 'major', 'language', 'vision')
    actions = [export_questionaire]

# for importing and exporting the experiment data
class SequencesResource(resources.ModelResource):
    class Meta:
        model = Sequences

class SequencesAdmin(ImportExportModelAdmin):
    resource_class = SequencesResource
    list_display = ('id','sequence','tally')
    readonly_fields = ('id','sequence','tally')

# for importing and exporting the experiment data
class ExperimentPageResource(resources.ModelResource):
    class Meta:
        model = ExperimentPage

class ExperimentPageAdmin(admin.ModelAdmin):
    list_display = ('pid','timestamp','question_number', 'image_ref')
    readonly_fields = ('pid','timestamp','question_number', 'answer', 'image_ref', 'gazedata')
    actions = [export_csv]


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(ExperimentPage, ExperimentPageAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Sequences, SequencesAdmin)



