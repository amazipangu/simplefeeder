from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField('created at')

class Entry(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField('created_at')
