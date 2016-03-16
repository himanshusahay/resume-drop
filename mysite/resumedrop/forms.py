from django import forms

class UploadFileForm(forms.Form):
	upload_file = forms.FileField(label='Select a file')