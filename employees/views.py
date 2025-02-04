from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializer import EmployeeSerializer

class CreateEmployee(APIView):
    def post(self, request):
        try:
            # Validate required fields
            required_fields = ["name", "email", "age", "gender", "address"]
            for field in required_fields:
                if field not in request.data:
                    return Response({"message": "invalid body request", "success": False}, status=400)

            # Check if employee already exists with the same email
            if Employee.objects.filter(email=request.data["email"]).exists():
                print('comes in the view and checkk--------------------------------------------------------------')
                return Response({"message": "employee already exists", "success": False}, status=409)

            # Save employee
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                employee = serializer.save()
                return Response({"message": "employee created successfully", "regid": employee.regid, "success": True}, status=200)

            return Response({"message": "invalid body request", "success": False}, status=400)

        except Exception as e:
            return Response({"message": "employee creation failed", "success": False}, status=500)


class GetEmployee(APIView):
    def get(self, request):
        try:
            regid = request.GET.get("regid")
            if regid:
                employee = Employee.objects.filter(regid=regid).first()
                if not employee:
                    return Response({"message": "no employee found with this regid", "success": False}, status=200)
                serializer = EmployeeSerializer(employee)
                return Response({"message": "employee details found", "success": True, "employees": [serializer.data]}, status=200)
            
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response({"message": "employee details found", "success": True, "employees": serializer.data}, status=200)

        except Exception as e:
            return Response({"message": "employee details not found", "success": False, "employees": []}, status=500)



class UpdateEmployee(APIView):
    def put(self, request):
        try:
            regid = request.data.get("regid")
            print(regid, '------------------------==============================================')
            if not regid:
                return Response({"message": "invalid body request", "success": False}, status=400)

            employee = Employee.objects.filter(regid=regid).first()
            if not employee:
                return Response({"message": "no employee found with this regid", "success": False}, status=200)

            print(request.data, '=======================================================================================')
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "employee details updated successfully", "success": True}, status=200)

            return Response({"message": "invalid body request", "success": False}, status=400)

        except Exception as e:
            return Response({"message": "employee updation failed", "success": False}, status=500)



class DeleteEmployee(APIView):
    def delete(self, request):
        try:
            print('hey-----------------------------------------------------')
            regid = request.data.get("regid")
            print(regid, '----------------------------------------')
            if not regid:
                return Response({"message": "invalid body request", "success": False}, status=400)

            employee = Employee.objects.filter(regid=regid).first()
            if not employee:
                return Response({"message": "no employee found with this regid", "success": False}, status=200)

            employee.delete()
            return Response({"message": "employee deleted successfully", "success": True}, status=200)

        except Exception as e:
            return Response({"message": "employee deletion failed", "success": False}, status=500)
