from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login_instructor, name='login'),
    url(r'^log_out$', views.log_out, name='log_out'),
    url(r'^dashboard$', views.dashboard, name='dashboard')
]
