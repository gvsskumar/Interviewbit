from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from .models import Employee
from .serializers import EmployeeSerializer
import requests


# ✅ POST API (Create Employee)
@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ GET API (Fetch Employees)
@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


# ✅ GET API (Third-party API Example)
@api_view(['GET'])
def get_external_users(request):
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=5)
        return Response(response.json())
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# ✅ PUT API (Full Update)
@api_view(['PUT'])
def update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

    serializer = EmployeeSerializer(employee, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)


# ✅ PATCH API (Partial Update)
@api_view(['PATCH'])
def partial_update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

    serializer = EmployeeSerializer(employee, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)


# ✅ DELETE API
@api_view(['DELETE'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=404)

    employee.delete()
    return Response({"message": "Deleted successfully"}, status=204)