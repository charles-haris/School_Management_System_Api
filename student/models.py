from django.db import models
from user.models import CustomUser
from parent.models import Parent

# Create your models here.
class Statut(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    GRADUATED = "graduated", "Graduated"
    SUSPENDED= "suspended", "Suspended"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete= models.CASCADE )
    student_number = models.CharField(unique=True, max_length=20, blank=False)
    middle_name = models.CharField(max_length=30)
    admission_date = models.DateField()
    statut = models.CharField(max_length=10, choices=Statut.choices , default=Statut.ACTIVE)
    profile_image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




