from django.contrib import admin

# Register your models here.
from .models import DotsEyegaze

class DotsEyegazeAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp','id')
    list_display = ('user','timestamp','id')

admin.site.register(DotsEyegaze, DotsEyegazeAdmin)