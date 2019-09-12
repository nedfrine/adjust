from django.db import models

# Create your models here.

from django.db import models


class Click(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=128)
    country = models.CharField(max_length=16)
    os = models.CharField(max_length=32)
    impressions = models.IntegerField()
    clicks = models.PositiveIntegerField()
    installs = models.PositiveIntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
    cpi = models.FloatField(editable=True)

    def save(self, *args, **kwargs):
        self.cpi = self.spend / self.installs
        super(Click, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.date, self.channel, self.country, self.os, self.impressions,self.clicks, self.installs, self.spend, self.revenue, self.os,self.cpi)


