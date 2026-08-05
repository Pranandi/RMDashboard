from django.db import models # type: ignore

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    cuid = models.CharField(max_length=20, unique=True)
    employee_code = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    hired_date = models.DateField()
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey('Role.Role', on_delete=models.RESTRICT, related_name='employees')
    location = models.ForeignKey('Location.Location', on_delete=models.RESTRICT, related_name='employees')
    # Self-referential relation for the employee's manager (optional). Using a ForeignKey instead of an invalid SelectField.
    manager_name = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='direct_reports',
        null=True,
        blank=True,
        help_text='Optional direct manager (another employee).'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.employee_code}"
    
    class Meta:
        db_table = 'employees'
        ordering = ['first_name', 'last_name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        indexes = [
            models.Index(fields=['employee_code']),
            models.Index(fields=['cuid']),
            models.Index(fields=['email']),
        ]
        # Removed redundant UniqueConstraints for fields already declared unique=True.