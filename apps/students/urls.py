from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.StudentsView.as_view(), name='index'),
    url(r'^(?P<filter>\w+)$', views.StudentsView.as_view(), name='index_filter'),
    url(r'^get_students/(?P<filter>\w+)$', views.GetStudents.as_view()), #edit this shit
    url(r'^s/(?P<pk>\d+)$', views.StudentDetailsView.as_view(), name='details'),
    url(r'^s/update/(?P<pk>\d+)$', views.UpdateStudentView.as_view(), name='update'),
    url(r'^s/(?P<pk>\d+)/create_alias$', views.create_alias, name='create_alias'),
    url(r'^s/(?P<pk>\d+)/create_note$', views.create_note, name='create_note'),
]