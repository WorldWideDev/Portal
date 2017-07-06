from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.StudentView.as_view(), name='index'),
    url(r'^(?P<filter>\w+)$', views.StudentView.as_view(), name='index_filter')
]