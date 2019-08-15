from django.db import models


class PhoneCatalog(models.Model):
    LastName = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    RegDate = models.DateTimeField('date published')
