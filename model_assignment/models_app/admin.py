from django.contrib import admin
from .models import School, CertificateType, Faculty, Grade, Department, Student

# Register your models here.
admin.site.register(School)
admin.site.register(CertificateType)
admin.site.register(Faculty)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Student)
