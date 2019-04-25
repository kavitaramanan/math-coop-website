from django.contrib import admin
from .models import *
# Register your models here.

class PresentationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Presentation, PresentationAdmin)

class FileAdmin(admin.ModelAdmin):
    pass
admin.site.register(File, FileAdmin)

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, PersonAdmin)

class OutreachAdmin(admin.ModelAdmin):
    filter_horizontal = ("people",) 
admin.site.register(Outreach, OutreachAdmin)
