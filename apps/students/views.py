# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import CreateStudentForm
from .view_helpers import set_context

INDEX_TEMPLATE = 'students/index.html'
DEFAULT_STUDENT_FILTER = 'active'

class StudentView(View):

    def get(self, req, filter=DEFAULT_STUDENT_FILTER):

        #helper function to initialize context with correct filter query on students
        context = set_context(filter)

        return render(req, INDEX_TEMPLATE, context)

    def post(self, req, filter):
        context = set_context(filter)
        form = CreateStudentForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("students:index"))
        context["form"] = form 
        return render(req, INDEX_TEMPLATE, context)        


