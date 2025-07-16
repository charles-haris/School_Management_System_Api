from django.db import models

# Create your models here.
class Status(models.TextChoices):
    ACTIVE = "Active", "active"
    INACTIVE = "Inactive", "inactive"
    COMPLETED = "Completed", "completed"

class Academic_year(models.Model):
    year_name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=Status, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


