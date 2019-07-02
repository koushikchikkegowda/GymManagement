from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# from treebeard.mp_tree import MP_Node


# Create your models here.

class membership(models.Model):
    type = models.CharField(max_length=200)  #pt or normal
    price =  models.IntegerField()
    duration =  models.IntegerField()

class Customer(AbstractBaseUser):
    name = models.CharField(max_length=250, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    membership = models.ForeignKey(membership, on_delete=models.SET_NULL, blank=True,null=True)


class Employee(AbstractBaseUser):
    name = models.CharField(max_length=250, unique=True)
    joining = models.DateTimeField(blank=True,null=True)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

class sales(models.Model):
    type = models.CharField(max_length=200)
    amount =  models.IntegerField()
    duration =  models.IntegerField()
    date = models.DateTimeField(blank=True,null=True)
    Employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True,null=True)

