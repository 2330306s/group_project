from django.contrib import admin
from investart.models import DevProfile, InvProfile, Project, Contact

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('project_name',)}

class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(DevProfile)
admin.site.register(InvProfile)
