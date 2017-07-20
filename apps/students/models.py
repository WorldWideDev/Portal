# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..course_sessions.models import Session, Cohort
from ..login.models import Instructor

# might consider making this a query set class rather than manager
class StudentManager(models.Manager):
    def student_filter(self, **kwargs):
        if str(kwargs['filter']) != 'all':
            return self.filter(status=str(kwargs['filter']))
        return self.all()

    def add_to_session(self, data):
        students = data.getlist('to_assign')
        sesh_id = int(data['session'])
        co_id = int(data['cohort_id'])
        for s in students:
            student = self.get(id=s)

            # remove sessions that conflict with new session start date
            conflict = student.session_history.filter(start_date_id=co_id).first()
            if conflict:
                student.session_history.remove(conflict)

            student.session_history.add(sesh_id)

    def assignment_filter(self, filter_kw, start_id):
        return self.filter(session_history__start_date_id = start_id).filter(status='active') \
            if str(filter_kw) == "assigned" else \
            self.exclude(session_history__start_date_id = start_id).filter(status='active')

    


class Student(models.Model):
    ACTIVE = 'active'
    PAUSED = 'paused'
    DROPPED = 'dropped'
    GRADUATED = 'graduated'

    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (PAUSED, "Paused"),
        (DROPPED, "Dropped"),
        (GRADUATED, "Graduated")
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(
        choices=STATUS_CHOICES,
        default=ACTIVE,
        max_length=20
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_cohort = models.ForeignKey(Cohort)
    session_history = models.ManyToManyField(Session, related_name='students', blank=True)

    def last_session(self):
        return self.session_history.last()

    def session_in_start_date(self, sesh_start_id):
        return self.session_history.filter(start_date_id=sesh_start_id).first()

    def has_rolled_back(self):
        sesh_dict = {}
        for sesh in self.session_history.all():
            print sesh
            try:
                sesh_dict[sesh.course.id]
                return sesh_dict[sesh.course.id]
            except KeyError:
                sesh_dict[sesh.course.id] = True                
        return False

    # def save(self, **kwargs):
    #     super(Student, self).save(**kwargs)
    
    def __unicode__(self):
        return self.email

    objects = StudentManager()

class Alias(models.Model):
    handle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    student = models.ForeignKey(Student, related_name='aliases')

class Note(models.Model):
    content = models.TextField()
    student = models.ForeignKey(Student, related_name='notes')
    created_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(Instructor)