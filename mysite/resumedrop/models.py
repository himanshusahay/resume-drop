from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils.encoding import python_2_unicode_compatible
# import os

# for student profile creation
# -------------

def content_file_name(instance, filename):
	return '/'.join(['resumedrop/static/polls', instance.wpi_username])


@python_2_unicode_compatible  # to support python 2
class Student(models.Model):
	wpi_username = models.CharField(max_length = 30, default="") # will store as _______ @wpi.edu # unique identifier
	name = models.CharField(max_length = 50, default="")
	class_year = models.CharField(max_length = 15, default="") # could be a master's student
	major = models.CharField(max_length = 80, default="")
	# where will the resumes be stored?
	resume = models.FileField(upload_to=content_file_name)
	
	def __str__(self):
		return self.name

# ------------- 

