import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
import django
django.setup()
from investart.models import Project

def populate():
    projects = {}

    for project, project_data in projects.items():
        p = add_project(project, project_data["overview"], project_data["fund_req"],
                        project_data["returns"], project_data["inn_score"])

def add_project(name, overview, fund_req, returns, inn_score):
    p = Project.objects.get_or_create(name=name, overview=overview, fund_req=fund_req,
                                      returns=returns, inn_score=inn_score)[0]
    p.inn_score=inn_score
    p.save()
    return p
                                      

if __name__ == '__main__':
    print("Starting investart population script...")
    populate()
    
