import email
from django.db import models
# Create your models here.



class StudentList(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    roll_no = models.IntegerField(default=0)
    address = models.CharField(max_length=30)
    pass

