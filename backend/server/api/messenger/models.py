from django.db import models


class UnreadMessage(models.Model):
    sender_name = models.CharField(max_length=100)
    scraper_run_time = models.IntegerField()
