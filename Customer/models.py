from django.db import models

class Company(models.Model):
    name = models.CharField(default="",max_length=200)
    logo = models.FileField(null=True,blank=True)
    description = models.TextField(default='',blank=True,null=True)
