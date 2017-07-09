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
    print ajacency, 'is adj'
    if ajacency:
        print 'we have ajancency'
        start_date_id = Cohort.objects.adjacent_cohort(start_date_id, ajacency).id
    return Student.objects.get(id=student_id).session_in_start_date(start_date_id)