from django.db import models

# Create your models here.
class UploaderVariant(models.Model):
    template_id = models.CharField(max_length=100)
    last_updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    project = models.CharField(max_length=255)
    variant_name = models.CharField(max_length=255)
    variant_description = models.TextField(blank=True, null=True)
    default_variant = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    impacting = models.BooleanField(default=False)
    mop = models.TextField(blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    team_description = models.TextField(blank=True, null=True)
    variant = models.CharField(max_length=255, blank=True, null=True)
    default_project_variant = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.template_id} - {self.variant_name}"

    class Meta:
        db_table = 'uploader_variants'
        verbose_name = 'Uploader Variant'
        verbose_name_plural = 'Uploader Variants'
        ordering = ['template_id', 'variant_name']
