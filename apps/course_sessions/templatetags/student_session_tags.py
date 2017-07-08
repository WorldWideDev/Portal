from django import template
from ...students.models import Student

register = template.Library()

'''
USEAGE: {% assigned_session student.id start_date.id %}
returns instance of assigned session or None

REMEBER: you must include {% load student_session_tags %} in body of template
'''

@register.simple_tag
def assigned_session(student_id, start_date_id):
    return Student.objects.get(id=student_id).session_in_start_date(start_date_id)