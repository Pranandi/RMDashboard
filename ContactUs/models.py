from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    alternative_phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = 'contact_us'
        ordering = ['id']
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
        indexes = [
            models.Index(fields=['email']),
        ]
        constraints = []
        
    
    