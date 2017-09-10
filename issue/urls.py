from django.conf.urls import url
from django.contrib.auth import views as auth_views

from issue import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registrar-incidencia/$', views.add_issue, name='add_issue'),
]
