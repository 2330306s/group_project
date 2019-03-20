from django.contrib import admin
from investart.models import DevProfile, InvProfile, ModProfile, Project, Contact

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(DevProfile)
admin.site.register(InvProfile)
admin.site.register(ModProfile)
