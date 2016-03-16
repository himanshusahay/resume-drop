from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from .models import Student
from .forms import UploadFileForm


'''
Restrict access to success and authorized pages, (only if you have succeeded or only if you are logged in)

'''

# Create your views here.

def index(request):
	context = {}
	return render(request, 'resumedrop/index.html', context)

def student_create(request):
	# no session info for students
	context = {}
	return render(request, 'resumedrop/student_create.html', context)

def create_success(request):

	# Check if form is valid, then save form data
	if request.method == 'POST':
		try:
			wpi_username = request.POST['wpi_username']

			# handle resume upload
			form = UploadFileForm(request.POST, request.FILES)

			if form.is_valid():
				resume = request.FILES['upload_file']
			
				# do this if form is valid
				try:
					student_to_check = Student.objects.get(wpi_username__exact = wpi_username)
				
					# if this student exists, overwrite data
					student_to_check.name = request.POST['name'] 
					student_to_check.class_year = request.POST['class_year']
					student_to_check.major = request.POST['major']

					# # handle resume upload
					# form = UploadFileForm(request.POST, request.FILES)
					# if form.is_valid():
					# 	student_to_check.resume = request.FILES['upload_file']
					
					student_to_check.resume = resume	
					student_to_check.save()
					return HttpResponseRedirect(reverse('resumedrop:success_redirect'))
				
				# this student is a new one, will have to create a new entry in the db
				except (KeyError, Student.DoesNotExist):

					name = request.POST['name']
					class_year = request.POST['class_year']
					major = request.POST['major']

					# handle resume upload
					# form = UploadFileForm(request.POST, request.FILES)
					# if form.is_valid():
					# 	resume = request.FILES['upload_file']
					
					student_created = Student(wpi_username=wpi_username, name=name, class_year=class_year, major=major, resume=resume)
					student_created.save()
					
					return HttpResponseRedirect(reverse('resumedrop:success_redirect'))

			# if form is not valid
			else:
				# Redisplay form to submit data properly
				return render(request, 'resumedrop/student_create.html', {'error_message: "Information not inputted correctly"'})

		except KeyError:
			# Redisplay form to submit data properly
			return render(request, 'resumedrop/student_create.html', {'error_message: "Information not inputted correctly"'})


def success_redirect(request):
	return render(request, 'resumedrop/index.html', {'success': "Your student profile has been created. Good luck at the WPI Startup Career Fair!"})



# def company_main(request):
# 	return HttpResponse('Companies will see global list of students here')

# # this is the student profile seen by companies
# def student(request, id_main):
# 	name = Name.objects.get(identifier.id_main=id_main)
# 	return HttpResponse("Student: " % name)
