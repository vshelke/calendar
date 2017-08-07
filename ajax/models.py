from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    start = models.DateTimeField('start time')
    end = models.DateTimeField('end time')
    

