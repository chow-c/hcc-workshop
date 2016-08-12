from django.contrib import admin

# Register your models here.
from .models import NewsletterSignup

class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = ('signup_date',)
    list_display = ('email', 'signup_date')

admin.site.register(NewsletterSignup, NewsletterAdmin)