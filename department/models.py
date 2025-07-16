from django.db import models
from teacher.models import Teacher

# Create your models here.
class Status(models.TextChoices):
    ACTIVE = "Active", "active"
    INACTIVE = "Inactive", "inactive"

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_uuid =  models.UUIDField(unique=True)
    department_code =  models.CharField(max_length=10 ,unique=True)
    head_of_department = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices = Status, default= Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



