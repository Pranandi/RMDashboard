from django.db import models


class AipData(models.Model):
    server = models.CharField(max_length=255, blank=True, null=True)
    inst_comp_name = models.CharField(max_length=255, blank=True, null=True)
    primary_ip = models.CharField(max_length=50, blank=True, null=True)
    inst_comp_status = models.CharField(max_length=100, blank=True, null=True)
    aip_status = models.CharField(max_length=100, blank=True, null=True)
    vpdc_profile = models.CharField(max_length=255, blank=True, null=True)
    customer_site_id = models.CharField(max_length=100, blank=True, null=True)
    customer_site_name = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=50, blank=True, null=True)
    physical_site_id = models.CharField(max_length=100, blank=True, null=True)
    support_region = models.CharField(max_length=100, blank=True, null=True)
    sales_product_line = models.CharField(max_length=255, blank=True, null=True)
    service_package = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.server or str(self.id)

    class Meta:
        db_table = 'aip_data'
        verbose_name = 'AIP Data'
        verbose_name_plural = 'AIP Data'
        ordering = ['server']
