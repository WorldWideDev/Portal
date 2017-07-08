from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.login.urls', namespace='login')),
    url(r'^students/', include('apps.students.urls', namespace='students')),
    url(r'^sessions/', include('apps.course_sessions.urls', namespace='sessions')),
]
