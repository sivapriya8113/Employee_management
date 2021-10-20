from django.db import models


# Create your models here.
from django.db.models import options

"""class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title"""


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=5)
    mobile = models.CharField(max_length=15)
    Email =models.EmailField(max_length=300,default='')
    Password =models.CharField(max_length=15,default='')
    Address =models.CharField(max_length=300,default='')
    EMPimage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,default='')





