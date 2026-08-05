from django.db import models

# Create your models here.
class task_information(models.Model):
    task_id = models.AutoField(primary_key=True)
    change_number = models.ForeignKey('Changedetails.ChangeDetails', on_delete=models.RESTRICT, related_name='taskinformations')
    company_name = models.CharField(max_length=100, null=True, blank=True)
    server_name = models.CharField(max_length=100)
    os = models.CharField(max_length=100, null=True, blank=True)
    environment = models.CharField(max_length=100, null=True, blank=True)
    environment_type = models.CharField(max_length=100, null=True, blank=True)
    stage = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    started_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)    
    manual_status = models.CharField(max_length=100, null=True, blank=True)
	
    def __str__(self):
        return  self.company_name + " - " + self.server_name + " - " + self.status
    
    class Meta:
        db_table = 'task_information'
        ordering = ["-updated_date", "-started_date"]
        verbose_name = 'task information'
        verbose_name_plural = 'task information'
        indexes = [
            models.Index(fields=['change_number']),
        ]