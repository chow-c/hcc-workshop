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
            'fields': ('author', 'name', 'description', 'start_date', 'end_date')
        }),
    )
    inlines = [QuestionInline, ResponseInline]

admin.site.register(Survey, SurveyAdmin)