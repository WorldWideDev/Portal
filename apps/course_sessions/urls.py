from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home_redirect, name='home'),
    url(r'^(?P<co_id>\d+)$', views.index, name='index_pattern'),
    url(r'^(?P<co_id>\d+)/(?P<filter_kw>\w+)$', views.index, name='index_filter'),
    url(r'^sesh/(?P<pk>\d+)$', views.SessionDetailView.as_view(), name='details'),
    url(r'^update_session$', views.update_session, name='update_session')
]