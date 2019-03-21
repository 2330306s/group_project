from django.contrib import admin
from investart.models import DevProfile, InvProfile, Project, Contact

#Adding the projects to the admin page
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('project_name',)}
 
#Adding to contact form details to the admin page
class ContactAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

#Registering everything with the admin site
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(DevProfile)
admin.site.register(InvProfile)
