from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
from .models import NewsletterSignup

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from home.models import WorkshopUser

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class WorkshopUserInline(admin.StackedInline):
    model = WorkshopUser
    can_delete = False
    verbose_name_plural = 'workshopUser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (WorkshopUserInline, )

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=HCCworkshop_subscriptions.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"email"),
        smart_str(u"signup_date"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.email),
            smart_str(obj.signup_date),
        ])
    return response
export_csv.short_description = u"Export CSV"

class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = ('signup_date',)
    list_display = ('email', 'signup_date')
    actions = [export_csv]

admin.site.register(NewsletterSignup, NewsletterAdmin)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)