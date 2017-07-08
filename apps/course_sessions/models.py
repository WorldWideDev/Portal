# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from ..login.models import Instructor

class SessionManager(models.Manager):
    def add_students(self, **kwargs):
        print kwargs
        pass

class CohortManager(models.Manager):
    def current_cohort(self):
        print now()
        curr = self.filter(starting_date__lt = now()).last()
        return curr
    def previous_cohort(self, id):
        this_cohort_starts = self.get(id=id).starting_date
        print this_cohort_starts
        return self.filter(starting_date__lt = this_cohort_starts).last()
    def next_cohort(self, id):
        this_cohort_starts = self.get(id=id).starting_date        
        return self.filter(starting_date__gt = this_cohort_starts).first()
        

class Cohort(models.Model):
    starting_date = models.DateTimeField()
    def __unicode__(self):
        return str(self.starting_date.strftime('%B %d, %Y'))
    class Meta:
        ordering = ['starting_date']
    objects =  CohortManager()

class ParentCourse(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(ParentCourse)
    def __unicode__(self):
        return self.name

class Session(models.Model):
    start_date = models.ForeignKey(Cohort)
    lecture_link = models.CharField(max_length=100)
    course = models.ForeignKey(Course)
    instructor = models.ForeignKey(Instructor)
    objects = SessionManager()
    def __unicode__(self):
        return "{} ({})".format(self.course, self.start_date.starting_date.strftime("%m/%d/%Y")) 
    