from django.db import models


class TimezoneTable(models.Model):
    time_zone = models.CharField(max_length=100)
    remedy_tz_dst_inactive = models.CharField(max_length=50, blank=True, null=True)
    remedy_tz_dst_active = models.CharField(max_length=50, blank=True, null=True)
    non_dst_offset_hours = models.CharField(max_length=20, blank=True, null=True)
    dst_offset = models.CharField(max_length=20, blank=True, null=True)
    offset_mins = models.CharField(max_length=20, blank=True, null=True)
    dst_start_time = models.CharField(max_length=50, blank=True, null=True)
    dst_end_time = models.CharField(max_length=50, blank=True, null=True)
    utc_offset = models.CharField(max_length=20, blank=True, null=True)
    daylight_savings_start = models.CharField(max_length=100, blank=True, null=True)
    daylight_savings_end = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.time_zone

    class Meta:
        db_table = 'timezone_table'
        verbose_name = 'Timezone'
        verbose_name_plural = 'Timezones'
        ordering = ['time_zone']
