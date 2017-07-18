# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.cache import cache
from django.views.generic import View, DetailView, UpdateView
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import CreateStudentForm, CreateAliasForm, CreateNoteForm, UpdateStudentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .view_helpers import set_context
from .models import Student
from django.contrib.auth.decorators import login_required

INDEX_TEMPLATE = 'students/index.html'
DETAILS_TEMPLATE = 'students/student_detail.html'
DEFAULT_STUDENT_FILTER = 'active'
STUDENTS_CACHE_KEY = "all_students"

class StudentsView(LoginRequiredMixin, View):
    def get(self, req, filter=DEFAULT_STUDENT_FILTER):

        #helper function to initialize context with correct filter query on students
        context = set_context(filter)

        return render(req, INDEX_TEMPLATE, context)

    def post(self, req, filter):
        context = set_context(filter)
        form = CreateStudentForm(req.POST)
        if form.is_valid():
            form.save()

            #Update cache after adding a new sutdent model
            Student.objects.update_student_cache()
            
            return HttpResponseRedirect(reverse("students:index"))
        return render(req, INDEX_TEMPLATE, context)        
        context["form"] = form

class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    template_name = 'students/student_update.html'

    def get_success_url(self):
        return reverse("students:details", kwargs={'pk':self.get_object().id})

    def form_valid(self, form):
        instance = form.save(commit=False)
        print form.data, 'is form'
        return super(UpdateStudentView, self).form_valid(form)
    # def post(self, req, pk):
    #     form = UpdateStudentForm(req.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse("students:show", kwargs={'pk':pk}))
    #     return render(req, self.template_name)

    # def get_context_data(self, *args, **kwargs):
    #     print self
    #     context = super(UpdateStudentView, self).get_context_data(*args, **kwargs)
    #     return context

class StudentDetailsView(LoginRequiredMixin, DetailView):
    model = Student
    def get_context_data(self, *args, **kwargs):
        context = super(StudentDetailsView, self).get_context_data(*args, **kwargs)
        context['alias_form'] = CreateAliasForm()
        context['note_form'] = CreateNoteForm()
        return context

    def post(self, req, pk):
        context = {
            "student": Student.objects.get(pk=pk)
        }
        print pk
        form = CreateAliasForm(req.POST)
        if form.is_valid():
            alias = form.save(commit=False)
            alias.student_id = pk
            alias.save()
        else:
            context["alias_form"] = CreateAliasForm(req.POST)

            return render(req, DETAILS_TEMPLATE, context)
        return HttpResponseRedirect(reverse("students:details", kwargs={'pk':pk}))

def create_alias(req, pk):
    if req.POST:
        context = {
            "student": Student.objects.get(pk=pk),
            "note_form": CreateNoteForm()
        }
        form = CreateAliasForm(req.POST)
        if form.is_valid():
            alias = form.save(commit=False)
            alias.student_id = pk
            alias.save()
        else:
            context["alias_form"] = form
            return render(req, DETAILS_TEMPLATE, context)
        return HttpResponseRedirect(reverse("students:details", kwargs={'pk':pk}))

def create_note(req, pk):
    if req.POST:
        context = {
            "student": Student.objects.get(pk=pk),
            "alias_form": CreateNoteForm()
        }
        form = CreateNoteForm(req.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student_id = pk
            note.instructor_id = req.user.id
            note.save()
        else:
            context["note_form"] = form
            return render(req, DETAILS_TEMPLATE, context)
        return HttpResponseRedirect(reverse("students:details", kwargs={'pk':pk}))