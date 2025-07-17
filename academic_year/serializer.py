from rest_framework import serializers
from .models import Academic_year

class Academic_yearSerializer (serializers.ModelSerializer):
    class Meta:
        model = Academic_year
        fields = '__all__'