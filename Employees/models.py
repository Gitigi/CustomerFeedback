from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserModel


class Employee(models.Model):

    firstname = models.CharField(null=False,blank=False,max_length=70)
    lastname = models.CharField(null=False,blank=False,max_length=70)
    passwd = models.CharField(null=False,blank=False,max_length=70)

    def save(self):
        username = self.firstname + self.lastname
        employe = UserModel.objects.create_user(username,password=self.passwd)
        employe.first_name = self.firstname
        employe.last_name = self.lastname

        employe.is_staff = False
        employe.is_superuser = False
        employe.save()
        super().save()

    def __str__(self):
        return (self.firstname + ' ' +self.lastname)
