from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import employees
from .serializers import EmployeeSerializer

@api_view(['POST'])
def create_employee(request):

    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Employee Created Successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)