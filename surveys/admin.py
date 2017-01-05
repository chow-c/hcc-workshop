from django.contrib import admin

from .models import Question, Survey, Response

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    classes = ['collapse']

class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0
    classes = ['collapse']

class SurveyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'start_date', 'end_date')
        }),
    )
    inlines = [QuestionInline, ResponseInline]

    def save_model(self, request, obj, form, change): 
        obj.author = request.user
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == Survey:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.author = request.user
                instance.save()
        else:
            formset.save()

admin.site.register(Survey, SurveyAdmin)