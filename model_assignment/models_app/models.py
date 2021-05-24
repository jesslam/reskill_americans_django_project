from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class CertificateType(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    grade_type = models.CharField(max_length = 255)
    def __str__(self):
        return self.grade_type

class Department(models.Model):
    name = models.CharField(max_length = 255)
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE) 

    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length = 255)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete = models.PROTECT)
    school = models.ForeignKey(School, on_delete = models.PROTECT)
    cert_type = models.ForeignKey(CertificateType, on_delete = models.PROTECT)

    def __str__(self):
        return self.fullname