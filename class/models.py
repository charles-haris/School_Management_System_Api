from django.db import models
from teacher.models import Teacher
from academic_year.models import Academic_year

# Create your models here.
class Status(models.TextChoices):
    ACTIVE = "Active" , "active"
    INACTIVE = "Inactive" , "inactive"
    

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    class_level = models.IntegerField() # grade level (1 - 12)
    section = models.CharField(max_length=10) #example section (A, B, C, etc.)
    capacity = models.IntegerField()
    current_strength = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=Status, default=Status.ACTIVE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(Academic_year, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)