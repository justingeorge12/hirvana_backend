from django.urls import path
from .views import CreateEmployee, GetEmployee, UpdateEmployee, DeleteEmployee

urlpatterns = [
    path('create_empl/', CreateEmployee.as_view(), name='workExperience'),
    path('get_empl/', GetEmployee.as_view(), name='get_empl'),
    path('update_empl/', UpdateEmployee.as_view(), name='get_empl'),
    path('delete_empl/', DeleteEmployee.as_view(), name='get_empl'),
]
