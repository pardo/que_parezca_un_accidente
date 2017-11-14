from django.conf.urls import url
from django.contrib.auth import views as auth_views

from issue import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registrar-incidencia/$', views.add_issue, name='add_issue'),
    url(r'^listado-incidencias/$', views.issue_list, name='issue_list'),
    url(r'^incidencia/(?P<issue_uuid>[-\w]+)/$', views.issue_view, name='issue_view'),
]
