from django.db import models

class Events(models.Model):
    yearstart = models.IntegerField(default=2023)
    yearend = models.IntegerField(default=2023)
    event = models.CharField(max_length=230)
