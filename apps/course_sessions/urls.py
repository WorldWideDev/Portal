from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)$', views.index, name='index_pattern'),
    url(r'^(?P<pk>\d+)/(?P<filter_kw>\w+)$', views.index, name='index_filter'),
    url(r'^update_session$', views.update_session, name='update_session')
]