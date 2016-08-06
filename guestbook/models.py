from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    personname = models.CharField(max_length=200)
    persondesc = models.TextField()
    pub_date = models.DateTimeField('date published')


class Contact(models.Model):
    mobile = models.CharField(max_length=200)
    nameofcpntact = models.CharField(max_length=200)
