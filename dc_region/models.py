from django.db import models

# Create your models here.
class DcRegion(models.Model):
	site_id = models.CharField(max_length=100)
	region = models.CharField(max_length=100)
	sub_region = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	scheduler_time_zone = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.site_id} - {self.region} - {self.city}"

	class Meta:
		db_table = 'dc_region'
		verbose_name = 'DC Region'
		verbose_name_plural = 'DC Regions'
		ordering = ['site_id', 'region']


