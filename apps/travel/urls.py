from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^registerprocess$', views.register),
    url(r'^loginprocess$', views.login),
    url(r'^travels', views.travels),
    url(r'^add$', views.add),
    url(r'^addTripProcess$', views.addTrip),
    url(r'^logout$', views.logout),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^destination/(?P<id>\d+)$', views.destination)


]
