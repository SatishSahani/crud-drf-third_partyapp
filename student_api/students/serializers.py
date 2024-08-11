# students/serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_roll(self, value):
        if value < 0:
            raise serializers.ValidationError("Roll number cannot be negative.")
        return value



# students/serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

    def validate_roll(self, value):
        """
        Check that the roll number is positive and unique.
        """
        if value <= 0:
            raise serializers.ValidationError("Roll number must be positive.")
        if Student.objects.filter(roll=value).exists():
            raise serializers.ValidationError("Roll number must be unique.")
        return value

    def validate_name(self, value):
        """
        Check that the name is not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_city(self, value):
        """
        Ensure that the city name is provided.
        """
        if not value.strip():
            raise serializers.ValidationError("City cannot be empty.")
        return value
