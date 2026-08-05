from django.db import models
import os
import uuid
from django.utils.text import slugify

# Create your models here.
def customer_logo_upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    ext = ext.lower() or '.png'
    slug = slugify(getattr(instance, 'name')) or 'name'
    unique = uuid.uuid4().hex
    return f"customer_logo/{slug}-{unique}{ext}"
class Customer(models.Model):
    name = models.CharField(max_length=30,unique=True)
    contact_person_name = models.CharField(max_length=30)
    contact_person_email = models.EmailField()
    contact_person_phone = models.CharField(max_length=15, blank=True, null=True)
    confluence_page_link = models.URLField(blank=True, null=True)
    customer_webpage     = models.URLField(blank=True, null=True)
    customer_logo      = models.ImageField(upload_to=customer_logo_upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'customers'
        ordering = ['name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['contact_person_email']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_customer_name'),
        ]