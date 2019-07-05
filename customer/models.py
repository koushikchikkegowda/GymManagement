from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# from treebeard.mp_tree import MP_Node


# Create your models here.

class membership(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    type = models.CharField(max_length=200)  #pt or normal
    price =  models.IntegerField()
    duration =  models.IntegerField()
    class Meta:
        db_table = 'membership'
    def __str__(self):
        return str(self.title)

class Employee(models.Model):
    name = models.CharField(max_length=250, unique=True)
    joining = models.DateTimeField(blank=True,null=True)
    designation = models.CharField(max_length=200)
    status = models.CharField(max_length=200,blank=True,null=True)
    address = models.TextField()
    phone = models.CharField(max_length=200)
    class Meta:
        db_table = 'Employee'
    def __str__(self):
        return str(self.name)
class Customer(models.Model):
    name = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=200,blank=True,null=True)
    membership = models.ForeignKey(membership, on_delete=models.SET_NULL, blank=True,null=True)
    address = models.TextField()
    phone = models.CharField(max_length=200)
    

    class Meta:
        db_table = 'Customer'
    def __str__(self):
        return str(self.name)


class sales(models.Model):
    type = models.CharField(max_length=200)
    amount =  models.IntegerField()
    duration =  models.IntegerField()
    date = models.DateTimeField(blank=True,null=True)
    Employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True,null=True)
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
    class Meta:
        db_table = 'sales'
    # def __str__(self):
    #     return self.date