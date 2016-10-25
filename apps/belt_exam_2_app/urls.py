from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^additem$', views.additem, name="additem"),
    url(r'^details/(?P<id>\d+)', views.details, name="details"),
    url(r'^join/(?P<id>\d+)', views.join, name="join"),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^remove/(?P<id>\d+)', views.remove, name="remove"),
    url(r'^delete/(?P<id>\d+)', views.delete, name="delete")
]
