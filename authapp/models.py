import profile
from statistics import mode
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    # image = models.ImageField(upload_to='images/', null=True)
    image = models.ImageField(null = True , blank = True)


class Information(models.Model):
    username = models.CharField(max_length=224,null= True)
    name = models.CharField(max_length=224,null= True)
    description = models.TextField(max_length=225,null= True)
    field = models.CharField(max_length=10,null= True)
    image = models.ImageField(upload_to='Media2',null=True,blank = True)  
    targetMarket = models.CharField(max_length=10,null= True)
    marketSize = models.CharField(max_length=10,null=True)
    marketSize1 = models.CharField(max_length=10,null=True)
    marketSize2 = models.CharField(max_length=10,null=True)
    marketSize3 = models.CharField(max_length=10,null=True)


