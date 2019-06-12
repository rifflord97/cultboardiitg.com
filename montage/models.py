from django.db import models


class Club_sec(models.Model):
    image = models.FileField(upload_to='./montage/cs')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email_us = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)


class Gallery(models.Model):
    image = models.FileField(upload_to='./montage/gallery')


class Youtube(models.Model):
    video = models.CharField(max_length=1000)


class Club_Member(models.Model):
    image1 = models.FileField(upload_to='./montage/cm',blank=True, null=True)
    name1 = models.CharField(max_length=100, blank=True, null=True)
    facebook1 = models.CharField(max_length=100, blank=True, null=True)
    instagram1 = models.CharField(max_length=100, blank=True, null=True)
    image2 = models.FileField(upload_to='./montage/cm', blank=True, null=True)
    name2 = models.CharField(max_length=100, blank=True, null=True)
    facebook2 = models.CharField(max_length=100, blank=True, null=True)
    instagram2 = models.CharField(max_length=100, blank=True, null=True)
    image3 = models.FileField(upload_to='./montage/cm', blank=True, null=True)
    name3 = models.CharField(max_length=100, blank=True, null=True)
    facebook3 = models.CharField(max_length=100, blank=True, null=True)
    instagram3 = models.CharField(max_length=100, blank=True, null=True)


class Acheivement(models.Model):
    acheivement = models.CharField(max_length=500)


class Imp_Link(models.Model):
    link = models.CharField(max_length=100)
    about = models.CharField(max_length=300)
