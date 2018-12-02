from django.contrib import admin
from .models import *
# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic, TopicAdmin)

class PresentationAdmin(admin.ModelAdmin):
    filter_horizontal = ("topics",) 
admin.site.register(Presentation, PresentationAdmin)

class FileAdmin(admin.ModelAdmin):
    pass
admin.site.register(File, FileAdmin)

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

class OutreachAdmin(admin.ModelAdmin):
    pass
admin.site.register(Outreach, OutreachAdmin)

# class PresentationTopicAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(PresentationTopic, PresentationTopicAdmin)
