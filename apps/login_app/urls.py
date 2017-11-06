from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.login, name = 'logPage' ),
    url(r'^register$', views.register, name = 'regPage'),
    url(r'^login_process$', views.login_process, name = 'login'),
    url(r'^register_process$', views.register_process, name = 'register')
]
