from django.db import models

# Create your models here.
class ChangeDetails(models.Model):
    change_id = models.AutoField(primary_key=True)
    change_number = models.CharField(max_length=100,unique=True)
    title = models.TextField()
    type = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100)
    zerotouch = models.BooleanField(default=False)
    startdate = models.DateTimeField(null=True, blank=True)
    enddate = models.DateTimeField(null=True, blank=True)
    remedy_status = models.CharField(max_length=100, null=True, blank=True)
    remedy_reason = models.CharField(max_length=255, null=True, blank=True)
    change_status = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    FINAL_STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
        ('Partial', 'Partial'),
        ('Unknown', 'Unknown'),
    ]
    final_status = models.CharField(max_length=20, choices=FINAL_STATUS_CHOICES, default='Unknown')
    
    def __str__(self):
        return self.change_number
    
    class Meta:
        db_table = 'change_details'
        ordering = ['change_number']
        verbose_name = 'Change Detail'
        verbose_name_plural = 'Change Details'
        indexes = [
            models.Index(fields=['change_number']),
        ]
        