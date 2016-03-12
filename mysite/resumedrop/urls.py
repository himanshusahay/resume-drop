from django.conf.urls import url

from . import views

app_name = 'resumedrop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_success/$', views.create_success, name='create_success'),
    url(r'^success/$', views.success_redirect, name='success_redirect'), 
    # ex: resumedrop/student_create
    url(r'^student_create/$', views.student_create, name='student_create'),
]