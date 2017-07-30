# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..students.models import Student
from .models import Session, Cohort, Course
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.apps.registry import apps

MAIN_TEMPLATE = 'course_sessions/index.html'

@login_required
def home_redirect(req):
    sesh = Session.objects.users_current_session_or_none(req.user.id, Cohort.objects.current_cohort_id())
    if sesh:
        return HttpResponseRedirect(reverse("sessions:details", kwargs={"pk": sesh.id}))
    return HttpResponseRedirect(reverse("sessions:index"))

@login_required
# this view will default to show sessions for the 'current' cohort
def index(req, co_id=Cohort.objects.current_cohort_id(), filter_kw="unassigned"):
    try:
        prev_id = Cohort.objects.previous_cohort(co_id).id
    except:
        prev_id = None
    try:
        next_id = Cohort.objects.next_cohort(co_id).id
    except:
        next_id = None
    
    context = {
        "students": Student.objects.assignment_filter(filter_kw, co_id),
        "session_start": Cohort.objects.get(id=co_id),
        "sessions": Session.objects.filter(start_date_id=co_id),
        "prev_id": prev_id,
        "next_id": next_id,
        "ass_filter": ["unassigned", "assigned"]
    }
    return render(req, MAIN_TEMPLATE, context)

class SessionDetailView(LoginRequiredMixin, DetailView):
    model = Session

def update_session(req):
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