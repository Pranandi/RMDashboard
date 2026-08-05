from django.db import models

# Create your models here.
class CrqClientApproval(models.Model):
	client = models.ForeignKey('clients.Clients', on_delete=models.CASCADE)
	template = models.ForeignKey('uploader_projects.UploaderProject', on_delete=models.CASCADE)
	approval_note = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.client} - {self.template}"

	class Meta:
		db_table = 'crq_client_approval'
		verbose_name = 'CRQ Client Approval'
		verbose_name_plural = 'CRQ Client Approvals'
		ordering = ['client', 'template']
