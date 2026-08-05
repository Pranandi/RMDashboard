from django.db import models

# Create your models here.
class CrqAdditionalTask(models.Model):
    task_name = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    assignee = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.task_name} - {self.assignee}"

    class Meta:
        db_table = 'crq_additional_tasks'
        verbose_name = 'CRQ Additional Task'
        verbose_name_plural = 'CRQ Additional Tasks'
        ordering = ['task_name']
        indexes = [
            models.Index(fields=['task_name']),
            models.Index(fields=['assignee']),
        ]