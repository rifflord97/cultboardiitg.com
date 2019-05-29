from django.db import models

class Events_Team(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    fb = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

class Club_Secy(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    fb = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

class Chairman(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    fb = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

class GenSec(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    fb = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

class Ev_Manager(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    fb = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)