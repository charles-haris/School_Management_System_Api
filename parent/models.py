from django.db import models
from user.models import CustomUser

# Create your models here.
class Relationship(models.TextChoices):
    FATHER = "Father", "father"
    MOTHER = "Mother", "mother"
    GUARDIAN = "Guardian", "guardian"
    OTHER = "Other", "other"


class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=10, choices=Relationship, default=Relationship.FATHER)
    occupation = models.CharField(max_length=100)
    emergency_contact = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

