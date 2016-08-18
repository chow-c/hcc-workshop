from django.contrib import admin

from .models import ImageEyegaze

# Register your models here.
class ImageEyegazeAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp','id')
    list_display = ('user','timestamp','id')

admin.site.register(ImageEyegaze,ImageEyegazeAdmin)