from django.db import models
from user.models import CustomUser

# Create your models here.

class Qualification(models.TextChoices):
    DEGREE = "Degree", "degree"
    MASTER_DEGREE = "Master Degree", "master degree"
    PHD = "Phd", "phd"

class Status(models.TextChoices):
    ACTIVE = "Active" , "active"
    INACTIVE = "Inactive" , "inactive"
    ON_LEAVE = "On Leave" , "on leave"
    

class Teacher(models.Model):
    employee_number = models.UUIDField()
    middle_name = models.CharField(max_length=20)
    hire_date = models.DateTimeField(auto_now_add=True)
    subject_specialization = models.CharField(max_length=20)
    qualification = models.CharField(max_length= 15 , choices=Qualification, default=Qualification.DEGREE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status, default=Status.ACTIVE)
    Profile_image = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





