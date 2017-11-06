from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.index, name='homepage'),
    url(r'^add_trip$', views.add_trip, name='add_trip'),
    url(r'^add_process$', views.add_trip_process, name = 'add'),
    url(r'^destination/(?P<id>\d+)$', views.destination, name='destination'),
    url(r'^logout$', views.log_out, name='logout'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join'),
    url(r'^not_join/(?P<id>\d+)$', views.not_join, name='join'),
    
]
