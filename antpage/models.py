from django.db import models
import uuid
import psycopg2
from django.contrib.auth.models import User
# Create your models here.
class event(models.Model):
    eno=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=255)
    elocation=models.CharField(max_length=255)
    edate=models.DateField()
    etime=models.TimeField()
    image = models.CharField(max_length=500,null=True)
    elike=models.CharField(max_length=1,default='f')
   