from django.db import models

# Create your models here.
class Version(models.Model):
    project = models.ForeignKey('Project.Project', on_delete=models.RESTRICT, related_name='versions')
    operation_system = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    policy_name = models.CharField(max_length=100, unique=True)
    manual_file_name = models.CharField(max_length=100)
    manual_file_location = models.CharField(max_length=100)
    confluence_page_link = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.project.name} - {self.version} ({self.operation_system})"
    
    class Meta:
        db_table = 'versions'
        ordering = ['project', '-version','operation_system']
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
        indexes = [
            models.Index(fields=['policy_name']),
            models.Index(fields=['project', 'operation_system', 'version']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['project', 'operation_system', 'version','policy_name'], name='unique_project_os_version_policy_name'),
        ]