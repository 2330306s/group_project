import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
import django
django.setup()
from investart.models import Project, Contact

def populate():
    projects = {}
    contacts = {}

    for project, project_data in projects.items():
        p = add_project(project, project_data["email"], project_data["project_website"],
                        project_data["overview"], project_data["fund_requirement"],
                        project_data["returns"], project_data["verified"], project_data["innovation_score"],
                        project_data["competition_score"])

    for contact, contact_data in contacts.items():
        c = add_contact(contact, contact_data["email"], contact_data["concern"],)

def add_project(project_name, email, project_website, overview, fund_requirement, returns, verified, innovation_score, competition_score):
    p = Project.objects.get_or_create(project_name=name, email=email, project_website=project_website, overview=overview,
                                      fund_requirement=fund_requirement, returns=returns, verified=verified,
                                      innovation_score=innovation_score, competition_score=competition_score)[0]
    p.verified=verified
    p.innovation_score=innovation_score
    p.competition_score=competition_score
    p.save()
    return p

def add_contact(name, email, concern):
    c = Contact.objects.get_or_create(name=name, email=email, concern=concern)[0]
    c.save()
    return c
                                      

if __name__ == '__main__':
    print("Starting investart population script...")
    populate()
    
