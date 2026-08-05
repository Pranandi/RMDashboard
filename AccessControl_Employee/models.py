from django.db import models
from Employee.models import Employee
# Create your models here.
class AccessControl_Employee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=200)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_export = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.employee.username} - {self.app_name}"
    
    class Meta:
        unique_together = ('employee', 'app_name')
        verbose_name = 'Access Control Employee'
        verbose_name_plural = 'Access Control Employees'
        db_table = 'accesscontrol_employee'
