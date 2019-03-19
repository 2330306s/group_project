import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')

import django
django.setup()

def populate():
    None

if _name_ == '_main_':
    print("Starting investart population script...")
    populate()
    
