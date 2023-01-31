from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=200,blank=True)
    link = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name=models.CharField(max_length=150)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    actype=models.CharField(max_length=50)
    material=models.TextField()

    def __str__(self):
        return self.name

