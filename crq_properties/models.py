from django.db import models

# Create your models here.
class CrqProperties(models.Model):
	is_impacting = models.BooleanField(default=False)
	change_type = models.CharField(max_length=100,choices=[('Service / Normal Maintenance','Service / Normal Maintenance'),('Customer Change','Customer Change'),('Emergency Maintenance','Emergency Maintenance')])
	manager_group = models.CharField(max_length=100,choices=[('Infra Change','Infra Change'),('Client Change','Client Change')])
	class1 = models.CharField(max_length=100, db_column='class',choices=[('No Impact','No Impact'),('Standard','Standard'),('Normal','Normal'),('Emergency','Emergency'),('Expedited','Expedited')])
	impact = models.CharField(max_length=100,choices=[('1-Extensive/Widespread','1-Extensive/Widespread'),('2-Significant/Large','2-Significant/Large'),('3-Moderate/Limited','3-Moderate/Limited'),('4-Minor/Localized','4-Minor/Localized')])
	urgency = models.CharField(max_length=100,choices=[('1-Critical','1-Critical'),('2-High','2-High'),('3-Medium','3-Medium'),('4-Low','4-Low')])
	risk_level = models.CharField(max_length=100,choices=[('Risk Level 1','Risk Level 1'),('Risk Level 2','Risk Level 2'),('Risk Level 3','Risk Level 3'),('Risk Level 4','Risk Level 4'),('Risk Level 5','Risk Level 5')])
	estimated_outage_duration = models.CharField(max_length=100,choices=[('No Disruption (Default)','No Disruption (Default)'),('1 to 50 msec','1 to 50 msec'),('51 msec to 1 min','51 msec to 1 min'),('1 min to 5 min','1 min to 5 min'),('1 min to 10 min','1 min to 10 min'),('1 min to 15 min','1 min to 15 min'),('10 min to 30 min','10 min to 30 min'),('30 min to 1 hour','30 min to 1 hour'),('1 hour to 2 hours','1 hour to 2 hours'),('1 hour to 3 hours','1 hour to 3 hours'),('1 hour to 4 hours','1 hour to 4 hours'),('1 hour to 5 hours','1 hour to 5 hours'),('1 hour to 6 hours','1 hour to 6 hours'),('1 hour to 7 hours','1 hour to 7 hours'),('1 hour to 8 hours','1 hour to 8 hours')])
	operational_categorization_1 = models.CharField(max_length=100,choices=[('Customer','Customer'),('IT','IT'),('Hosting','Hosting')])
	operational_categorization_2 = models.CharField(max_length=100,choices=[('Internal','Internal'),('OS Patch/Agent Upgrade','OS Patch/Agent Upgrade'),('Hosting Network Services','Hosting Network Services')])
	service_impact_assessment_work_info = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.change_type} - {self.manager_group}"

	class Meta:
		db_table = 'crq_properties'
		verbose_name = 'CRQ Properties'
		verbose_name_plural = 'CRQ Properties'
		ordering = ['change_type', 'manager_group']
