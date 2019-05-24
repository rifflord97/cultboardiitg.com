from django.db import models


class About(models.Model):
    about_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.about_text


class Upcoming_Events(models.Model):
    image = models.FileField()
    event_title = models.CharField(max_length=30)
    event_details = models.TextField()
    date = models.CharField(max_length=20, blank=True, null=True)
    venue = models.CharField(max_length=20, blank=True, null=True)


class Team(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    fb = models.CharField(max_length=50, blank=True, null=True)
    insta = models.CharField(max_length=50, blank=True, null=True)

