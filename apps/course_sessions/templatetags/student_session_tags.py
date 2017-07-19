from django import template
from ...students.models import Student
from ..models import Cohort
register = template.Library()

'''
USEAGE: {% assigned_session student.id start_date.id ajacency (OPTIONAL) %}
returns instance of assigned session or None

REMEBER: you must include {% load student_session_tags %} in body of template
'''

@register.simple_tag
def assigned_session(student_id, start_date_id, ajacency=None):
    if ajacency:
        adj_start_date = Cohort.objects.adjacent_cohort(start_date_id, ajacency)
        if adj_start_date:
            start_date_id = adj_start_date.id
        else:
            return None
    return Student.objects.get(id=student_id).session_in_start_date(start_date_id)

@register.simple_tag
def current_session_id():
    return Cohort.objects.current_cohort_id()