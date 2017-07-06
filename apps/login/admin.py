# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Instructor
from ..students.models import Student, Cohort, Note
from ..course_sessions.models import Session, Course, ParentCourse
# Register your models here.
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Note)
admin.site.register(Cohort)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(ParentCourse)
