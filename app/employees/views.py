from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import EmployeeSerializer
from .models import EmployeeModel

class AllEmployee(APIView):

    def get(self, request):
        
        employees = EmployeeModel.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return Response(employee_serializer.data)