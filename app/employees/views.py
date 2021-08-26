from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import EmployeeSerializer
from .models import EmployeeModel

class AllEmployee(APIView):

    def get(self, request):
        
        employees = EmployeeModel.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return Response(employee_serializer.data)


class AddEmployee(APIView):

    def post(self, request):

        employee_serializer = EmployeeSerializer(data=request.data)
        
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(employee_serializer.data)
        else:
            return Response('Did not work')

class SpecificEmployee(APIView):

    def get_object(self, id):
        try:
            return EmployeeModel.objects.get(id=id)
        except EmployeeModel.DoesNotExist:
            return Response('does not exist')
    
    def get(self, request, id):
        employee = self.get_object(id)
        employee_serializer = EmployeeSerializer(employee)
        return Response(employee_serializer.data)

    def delete(self, request, id):

        user = self.get_object(id)
        user_serializer = EmployeeSerializer(user)
        user.delete()
        return Response(user_serializer.data)
    
    def put(self, request, id):

        user = self.get_user(id)
        user_serializer = EmployeeSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response('Did not work')