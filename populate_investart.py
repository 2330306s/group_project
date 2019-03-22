#Population script

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
import django
django.setup()
from investart.models import Project, Contact

#Function to add projects, contact details from dictionaries
def populate():
    projects = {"ReVive": {"email": "bobbydentes@gmail.com", "project_website": "http://www.revive.com",
                           "overview": "Startup which aims at achieving global healthcare through tech", "fund_requirement": "1 million GBP",
                           "returns": "Investment+interest", "verified": "Yes", "innovation_score": "4/5", "competition_score": "3/5"},
                "Help'er": {"email": "daveredditor@gmail.com", "project_website": "",
                           "overview": "Startup which aims to empower women through tech", "fund_requirement": "500,000 GBP",
                           "returns": "Stake in the company", "verified": "No", "innovation_score": "Verification pending", "competition_score": "Verification pending"}
                }
    contacts = {"Dave": {"email": "daveredditor@gmail.com", "concern": "Hi, how long until my project is verified? Thanks"},
                "Aaron": {"email": "aaronaardvark@gmail.com", "concern": "Hey, A suggestion - please start a bidding system for investors! Thank you"}
                }

    for project, project_data in projects.items():
        p = add_project(project, project_data["email"], project_data["project_website"],
                        project_data["overview"], project_data["fund_requirement"],
                        project_data["returns"], project_data["verified"], project_data["innovation_score"],
                        project_data["competition_score"])

    for contact, contact_data in contacts.items():
        c = add_contact(contact, contact_data["email"], contact_data["concern"],)

#Function to get an object to be added
def add_project(project_name, email, project_website, overview, fund_requirement, returns, verified, innovation_score, competition_score):
    p = Project.objects.get_or_create(project_name=project_name, email=email, project_website=project_website, overview=overview,
                                      fund_requirement=fund_requirement, returns=returns, verified=verified,
                                      innovation_score=innovation_score, competition_score=competition_score)[0]
    p.verified=verified
    p.innovation_score=innovation_score
    p.competition_score=competition_score
    p.save()
    return p

#Function to get an object to be added
def add_contact(name, email, concern):
    c = Contact.objects.get_or_create(name=name, email=email, concern=concern)[0]
    c.save()
    return c
                                      

if __name__ == '__main__':
    print("Starting investart population script...")
    populate()
    
