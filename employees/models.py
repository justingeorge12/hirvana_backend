import uuid
from django.db import models

# def generate_regid():
#     """Generate a unique registration ID"""
#     last_employee = Employee.objects.order_by("-id").first()
#     if last_employee:
#         last_id = int(last_employee.regid.replace("EMP", "")) + 1
#     else:
#         last_id = 1
#     return f"EMP{last_id:03d}" 

class Employee(models.Model):
    # regid = models.CharField(max_length=10, unique=True, editable=False, default=generate_regid)
    regid = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, blank=True)
    address = models.JSONField()
    workExperience = models.JSONField()
    qualifications = models.JSONField()
    projects = models.JSONField()
    photo = models.ImageField(upload_to='profile/', null= True, blank=True)

    def save(self, *args, **kwargs):
        if not self.regid:
            last_employee = Employee.objects.order_by("-id").first()
            last_id = int(last_employee.regid.replace("EMP", "")) + 1 if last_employee else 1
            self.regid = f"EMP{last_id:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
