from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import ImagePage

# for importing and exporting the questions data
class imageResource(resources.ModelResource):
    class Meta:
        model = ImagePage

class imageAdmin(ImportExportModelAdmin):
    resource_class = imageResource
    list_display = ('id','answer','timestamp', 'image_number')

admin.site.register(ImagePage, imageAdmin)
