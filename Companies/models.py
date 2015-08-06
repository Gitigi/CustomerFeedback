from django.db import models

class Company(models.Model):
    name = models.CharField(default="",max_length=200)
    logo = models.FileField(null=True,blank=True)
    description = models.TextField(default='',blank=True,null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    firstname = models.CharField(default="",max_length=100)
    lastname = models.CharField(default='',max_length = 100)
    phone_no = models.CharField(default='',max_length = 100)
    feedback = models.CharField(default='',max_length = 100)
    company = models.ForeignKey(Company,default=None)

    def __str__(self):
        return self.lastname
