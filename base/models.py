from django.db import models

class PageVisits(models.Model):
    page_name = models.CharField(max_length=255)
    total_count = models.PositiveBigIntegerField(default=0)
