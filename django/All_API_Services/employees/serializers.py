from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    # Field-level validation
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be greater than 0")
        return value

    # Object-level validation
    def validate(self, data):
        if "test" in data['name'].lower():
            raise serializers.ValidationError("Invalid name")
        return data