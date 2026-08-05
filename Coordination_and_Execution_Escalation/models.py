from django.db import models

# Create your models here.
class CoordinationAndExecutionEscalation(models.Model):
    level = models.IntegerField(unique=True)
    description = models.CharField(max_length=255)
    location = models.ForeignKey('Location.Location', on_delete=models.RESTRICT, related_name='escalations')
    employees = models.ManyToManyField('Employee.Employee', related_name='escalations')
    contact_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Level {self.level} - {self.description}"
    
    class Meta:
        db_table = 'coordination_and_execution_escalations'
        ordering = ['level']
        verbose_name = 'Coordination and Execution Escalation'
        verbose_name_plural = 'Coordination and Execution Escalations'
        indexes = [
            models.Index(fields=['level']),
            models.Index(fields=['location']),
        ]    