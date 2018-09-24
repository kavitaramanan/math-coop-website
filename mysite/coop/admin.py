from django.contrib import admin

from coop.models import *

# Register your models here.
class PresentationFileAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(PresentationFile, PresentationFileAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Topic, TopicAdmin)