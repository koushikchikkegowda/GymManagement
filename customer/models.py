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
    status= models.CharField(max_length=200,blank=True,null=True)
    
    class Meta:
        db_table = 'membership'
    def __str__(self):
        return str(self.title)

class Employee(models.Model):
    name = models.CharField(max_length=250, unique=True)
    joining = models.DateField(blank=True,null=True)
    designation = models.CharField(max_length=200)
    status = models.CharField(max_length=200,blank=True,null=True,default="Active")
    address = models.TextField()
    phone = models.CharField(max_length=200)
    IdentityProof=models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        db_table = 'Employee'
    def __str__(self):
        return str(self.name)
class Customer(models.Model):
    name = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=200,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        else:            
            print("Save Override")
            print(self.title)
            url = "http://localhost:9200/Customer/doc/"+str(self.id)       

            payload = {
                "name":self.name,
                "address":self.address,
                "phone":self.phone,
            }
            headers = {'content-type': 'application/json'}
            response = requests.request(
                "PUT", url, data=json.dumps(payload),headers=headers)

            print(response.text)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Customer'
    def __str__(self):
        return str(self.name)


class sales(models.Model):
    NewOrOld = models.CharField(max_length=200,blank=True,null=True)  #Renewal or new
    startDate = models.DateField(blank=True,null=True)
    endDate = models.DateField(blank=True,null=True)
    PtOrNor = models.CharField(max_length=200,blank=True,null=True)
    Employee = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    customerName = models.CharField(max_length=200,blank=True,null=True)
    price = models.CharField(max_length=200,blank=True,null=True)
    class Meta:
        db_table = 'sales'
    # def __str__(self):
    #     return self.date