from django.db import models

# Create your models here.
class Location(models.Model):
    role = models.ForeignKey('Role.Role', on_delete=models.RESTRICT, related_name='locations',null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    working_hours = models.CharField(max_length=100)
    working_days = models.CharField(max_length=100, default='Monday to Friday')
    timezone = models.CharField(max_length=50, default='UTC')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return unique name of the location
        return self.name
    
    class Meta:
        db_table = 'locations'
        ordering = ['name']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        indexes = [
            models.Index(fields=['name'], name='location_name_idx'),
        ]
        