from __future__ import unicode_literals

from django.db import models
from django import forms


# for student profile creation
# -------------
class Wpi_email(models.Model):
    wpi_email_text = models.CharField(default='WPI Email', editable=False, max_length = 9)
    wpi_email_value = forms.CharField(max_length = 30)

class Name(models.Model):
	identifier = models.ForeignKey(Wpi_email, on_delete=models.CASCADE)
	name_text = models.CharField(default='Name', editable=False, max_length = 4)
	name_value = forms.CharField(max_length = 80)

class Class_year(models.Model):
	identifier = models.ForeignKey(Wpi_email, on_delete=models.CASCADE)
	class_year_text = models.CharField(default='Class Year', editable=False, max_length = 10)
	class_year_value = forms.CharField(max_length = 15) # could be a master's student

class Major(models.Model):
	identifier = models.ForeignKey(Wpi_email, on_delete=models.CASCADE)
	major_text = models.CharField(default='Major', editable=False, max_length = 4)
	major_value = forms.CharField(max_length = 80)

class Resume(models.Model):
	identifier = models.ForeignKey(Wpi_email, on_delete=models.CASCADE)
	resume_text = models.CharField(default='Resume', editable=False, max_length = 6)
	# where will the resumes be stored

# ------------- 

