from django.db import models

# Create your models here.
class CrqCoordination(models.Model):
	coordination = models.CharField(max_length=100)
	coordinator_company = models.CharField(max_length=100)
	coordinator_organization = models.CharField(max_length=100)
	workgroup = models.CharField(max_length=100)
	change_coordinator = models.CharField(max_length=100)
	task_name = models.CharField(max_length=100,blank=True, null=True)
	task_summary = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.coordination} - {self.workgroup}"

	class Meta:
		db_table = 'crq_coordination'
		verbose_name = 'CRQ Coordination'
		verbose_name_plural = 'CRQ Coordinations'
		ordering = ['coordination', 'workgroup']
