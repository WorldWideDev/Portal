# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..course_sessions.models import Session, Cohort
from ..login.models import Instructor

class StudentManager(models.Manager):
    def student_filter(self, **kwargs):
        print kwargs['filter']
        if str(kwargs['filter']) != 'all':
            print 'not all'
            return self.filter(status=str(kwargs['filter']))
        return self.all()

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

    def __unicode__(self):
        return self.email

    objects = StudentManager()

class Alias(models.Model):
    handle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    student = models.ForeignKey(Student)

class Note(models.Model):
    content = models.TextField()
    student = models.ForeignKey(Student)
    instructor = models.ForeignKey(Instructor)