from django.db import models

class Gallery(models.Model):
    image = models.FileField()

class Links(models.Model):
    calender = models.CharField(max_length=500, blank=True, null=True)
    results = models.CharField(max_length=500, blank=True, null=True)
    rulebook = models.CharField(max_length=500, blank=True, null=True)
    photos = models.CharField(max_length=500, blank=True, null=True)


