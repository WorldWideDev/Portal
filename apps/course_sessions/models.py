# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from ..login.models import Instructor

class CohortManager(models.Manager):
    def current_cohort(self):
        return self.filter(starting_date__lt = now()).last()
    def previous_cohort(self, id):
        this_cohort_starts = self.get(id=id).starting_date
        return self.filter(starting_date__lt = this_cohort_starts).last()
    def next_cohort(self, id):
        this_cohort_starts = self.get(id=id).starting_date        
        return self.filter(starting_date__gt = this_cohort_starts).first()
    def adjacent_cohort(self, id, ajacency):
        if ajacency == 'next':
            return self.next_cohort(id)
        return self.previous_cohort(id)
        

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
    def __unicode__(self):
        return "{} ({})".format(self.course, self.start_date.starting_date.strftime("%m/%d/%Y")) 
    