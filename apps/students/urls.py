from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.StudentsView.as_view(), name='index'),
    url(r'^(?P<filter>\w+)$', views.StudentsView.as_view(), name='index_filter'),
    url(r'^s/(?P<pk>\d+)$', views.StudentDetailsView.as_view(), name='details'),
    url(r'^s/(?P<pk>\d+)/create_alias$', views.create_alias, name='create_alias'),
    url(r'^st/(?P<pk>\d+)/create_note$', views.create_note, name='create_note'),
]