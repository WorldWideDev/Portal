# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..students.models import Student
from .models import Session, Cohort, Course
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, reverse

MAIN_TEMPLATE = 'course_sessions/index.html'

# this view will default to show sessions for the 'current' cohort
def index(req, pk=Cohort.objects.current_cohort().id, filter_kw="unassigned"):
    try:
        prev_id = Cohort.objects.previous_cohort(pk).id
    except:
        prev_id = None
    try:
        next_id = Cohort.objects.next_cohort(pk).id
    except:
        next_id = None

    context = {
        "students": Student.objects.assignment_filter(filter_kw, pk),
        "session_start": Cohort.objects.get(id=pk),
        "sessions": Session.objects.filter(start_date_id=pk),
        "prev_id": prev_id,
        "next_id": next_id,
        "ass_filter": ["unassigned", "assigned"]
    }
    return render(req, MAIN_TEMPLATE, context)

def update_session(req):
    print req.POST
    try: 
        req.POST.getlist('to_assign')
        Student.objects.add_to_session(req.POST)
    except KeyError:
        messages.error(req, "Please select a student to add")
        context = {
            "students": Student.objects.filter(status='active'),
            "start_dates": Cohort.objects.all(),
            "courses": Course.objects.all()
        }
        return render(req, MAIN_TEMPLATE, context)
    return HttpResponseRedirect(reverse("sessions:index"))