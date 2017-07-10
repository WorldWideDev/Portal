# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Instructor
from django.contrib.auth.admin import UserAdmin
from .forms import NewInstructorForm, ChangeInstructorForm
from ..students.models import Student, Cohort, Note
from ..course_sessions.models import Session, Course, ParentCourse
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.

class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    add_form = NewInstructorForm
    form = ChangeInstructorForm

admin.site.register(Instructor, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Note)
admin.site.register(Cohort)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(ParentCourse)
    