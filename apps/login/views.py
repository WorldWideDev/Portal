# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, get_user_model, login, logout, views as authviews
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect


LOGIN_TEMPLATE = 'login/index.html'
# DASHBOARD_TEMPLATE = 'login/dashboard.html'

# Create your views here.
def index(req):
    context = {
        'form': AuthenticationForm()
    }
    return render(req, LOGIN_TEMPLATE, context)

def login_instructor(req):
    print req
    submitted = AuthenticationForm(data=req.POST)
    if submitted.is_valid():
        user = submitted.get_user()
        #login(req, user)
        return HttpResponseRedirect(reverse('students:index'))
        # return reverse_lazy("students:index")
    context = {
        "form": submitted
    }
    return render(req, LOGIN_TEMPLATE, context)

def log_out(req):
    logout(req)
    return redirect('/')

#NOTE(Devon): this will get moved to some other app as we flesh out the app spec
#             testing the login_required feature
# @login_required
# def dashboard(req):
#     return reverse("students:index")