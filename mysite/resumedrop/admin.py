from django.contrib import admin

from .models import Wpi_email, Name, Class_year, Major, Resume

admin.site.register(Wpi_email)
admin.site.register(Name)
admin.site.register(Class_year)
admin.site.register(Major)
admin.site.register(Resume)
