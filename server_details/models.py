from django.db import models

# Create your models here.

class ServerDetails(models.Model):
    
    
    batch = models.IntegerField(choices=[(i, i) for i in range(1, 16)])
    client = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255,blank=True, null=True)
    application = models.CharField(max_length=255,blank=True, null=True)
    environment = models.CharField(max_length=255,blank=True, null=True)
    server_type = models.CharField(max_length=255,blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    include = models.BooleanField(choices=[(True, 'True'), (False, 'False')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.server} - {self.batch}"
    

    class Meta:
        db_table = 'server_details'
        verbose_name = 'Server Detail'
        verbose_name_plural = 'Server Details'
        ordering = ['batch', 'server']
