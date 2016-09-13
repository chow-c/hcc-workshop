from django.contrib import admin

from .models import DotsGaze, ReadingGaze, ImageGaze

class DotsGazeAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp','id')
    list_display = ('user','timestamp','id')

admin.site.register(DotsGaze, DotsGazeAdmin)

class ReadingGazeAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp','id')
    list_display = ('user','timestamp','id')

admin.site.register(ReadingGaze,ReadingGazeAdmin)

class ImageGazeAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp','id')
    list_display = ('user','timestamp','id')

admin.site.register(ImageGaze,ImageGazeAdmin)