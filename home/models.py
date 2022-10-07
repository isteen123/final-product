from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class clint(models.Model):
    GROUP_NAME = models.TextField(max_length=25, null=True,blank=True)
    AGENT=models.TextField(max_length=25, null=True,blank=True)
    EXAM_CODE=models.TextField(max_length=25, null=True,blank=True)
    DATE=models.DateField(null=True, blank=True)
    TIME=models.TimeField(null=True)
    LOCATION=models.TextField(max_length=25, null=True,blank=True)
    COMMENT=models.TextField(max_length=100, null=True,blank=True)
    ACTUALDATE=models.DateTimeField(null=True,blank=True)
    STASTUS=models.TextField(max_length=25, default = "took")
    T_ZONE=models.TextField(max_length=25, default = "Null")

class agent(models.Model):
    AGENT_NAME = models.TextField(max_length=25, null=True,blank=True)
    DOJ=models.DateField(null=True, blank=True)


class employee(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    EMP_ID=models.TextField(max_length=25,unique=True)
    EMP_NAME=models.TextField(max_length=25, null=True,blank=True)
    DOJ=models.DateField(null=True, blank=True) 