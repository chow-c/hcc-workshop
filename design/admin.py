from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Mappings

# for importing and exporting the questions data
class mappingsResource(resources.ModelResource):
    class Meta:
        model = Mappings

class mappingsAdmin(ImportExportModelAdmin):
    resource_class = mappingsResource
    list_display = ('id','answer','timestamp')

admin.site.register(Mappings, mappingsAdmin)