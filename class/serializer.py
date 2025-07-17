from rest_framework import serializers
from .models import Class

class ClassSerializer(serializers.ModelSerializer):
    teacher_full_name = serializers.SerializerMethodField()
    academic_year = serializers.CharField(source = 'academic_year.year_name', read_only=True)
    class Meta:
        model = Class
        fields = [
            'id', 'class_name', 'class_level', 'section', 'capacity', 'current_strength',
            'status', 'teacher_full_name', 'academic_year'
        ]

        def get_teacher_name(self, obj):
            #return obj.teacher.user.name if obj.teacher and obj.teacher.user else None
            return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"

