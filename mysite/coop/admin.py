from django.contrib import admin

from coop.models import *

# Register your models here.
class PresentationFileAdmin(admin.ModelAdmin):
    pass
class PresentationAdmin(admin.ModelAdmin):
    pass
class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(PresentationFile, PresentationFileAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Topic, TopicAdmin)