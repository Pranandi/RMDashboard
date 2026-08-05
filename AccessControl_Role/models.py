from django.db import models
from Role.models import Role
# Create your models here.
class AccessControl_Role(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=200)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_export = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.role.name} - {self.app_name}"
    
    class Meta:
        unique_together = ('role', 'app_name')
        verbose_name = 'Access Control Role'
        verbose_name_plural = 'Access Control Roles'
        db_table = 'accesscontrol_role'
