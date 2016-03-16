from django.conf.urls import url
from django.core import urlresolvers 

from django.contrib import admin
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'resumedrop'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_success/$', views.create_success, name='create_success'),
	url(r'^success/$', views.success_redirect, name='success_redirect'), 
	# ex: resumedrop/student_create
	url(r'^student_create/$', views.student_create, name='student_create'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)