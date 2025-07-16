from django.db import models
from department.models import Department

# Create your models here.
class Status(models.TextChoices):
    ACTIVE = "Active", "active"
    INACTIVE = "Inactive", "inactive"

class Subject(models.Model):
    subject_uuid = models.UUIDField(unique=True)
    subject_code = models.CharField(max_length=10, unique=True)
    subject_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    credits = models.IntegerField(default=1)
    department = models.ForeignKey(Department, on_delete =models.CASCADE)
    is_mandatory = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=Status, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





