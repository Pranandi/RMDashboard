from django.db import models

# Create your models here.
class UploaderProject(models.Model):
    template_id = models.CharField(max_length=100)
    project_id = models.CharField(max_length=100)
    project_title = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    change_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.template_id} - {self.project_id} - {self.change_title}"

    class Meta:
        db_table = 'uploader_projects'
        verbose_name = 'Uploader Project'
        verbose_name_plural = 'Uploader Projects'
        ordering = ['template_id', 'project_id']
