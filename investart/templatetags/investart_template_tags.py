from django import template
from investart.models import Project

register = template.Library()

@register.inclusion_tag('investart/projects.html')
def get_project_list(project=None):
    return {'projects': Project.objects.all(), 'act_project': project}
