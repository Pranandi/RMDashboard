from django.db import models

# Create your models here.
class Clients(models.Model):
    client_name = models.CharField(max_length=100)
    vantive_name = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    advanced_essential = models.CharField(max_length=20,choices=[('Advanced', 'Advanced'), ('Essential', 'Essential')])
    start_week = models.CharField(max_length=20,choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Penultimate', 'Penultimate'), ('Last', 'Last'), ('Specific Date', 'Specific Date'), ('First Weekday', 'First Weekday')])
    start_day = models.CharField(max_length=20,choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Specific Date', 'Specific Date'), ('First Weekday', 'First Weekday')])
    specific_date = models.DateField(blank=True, null=True)
    frequency = models.CharField(max_length=20,choices=[('Monthly', 'Monthly'), ('Bi-Monthly', 'Bi-Monthly'), ('Quarterly', 'Quarterly'), ('Request', 'Request')])
    add_month = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    ask_for_approval_in_email = models.BooleanField(default=False)
    email_greeting = models.CharField(max_length=255, blank=True, null=True)
    #multiple emails can be separated by commas
    email_to = models.CharField(max_length=255, blank=True, null=True)
    email_cc = models.CharField(max_length=255, blank=True, null=True)
    email_bcc = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.client_name}"
       
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['client_name']
        indexes = [
            models.Index(fields=['client_name']),
            models.Index(fields=['site_id']),
            models.Index(fields=['frequency']),
            models.Index(fields=['vantive_name']),
            models.Index(fields=['is_active']),
        ]
    
    