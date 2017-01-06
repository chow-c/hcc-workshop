from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Questionnaire, ExperimentPage, Questions, Sequences

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

class ExperimentPageAdmin(ImportExportModelAdmin):
    resource_class = ExperimentPageResource
    list_display = ('pid','timestamp','question_number', 'image_ref')
    readonly_fields = ('pid','timestamp','question_number', 'answer', 'image_ref', 'gazedata')

admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(ExperimentPage, ExperimentPageAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Sequences, SequencesAdmin)



