from django.db import models

# Create your models here.
from django.db.models.functions import datetime
from datetime import datetime


class student(models.Model):
    lname=models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    class_name=models.CharField(max_length=100)
    attendance=models.IntegerField(default=0)
    birthday=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return (self.fname)

class book(models.Model):
    namee = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)

    author=models.CharField(max_length=100,null=True)
    price=models.CharField(max_length=100,null=True)
    count=models.IntegerField(default=0)
    image=models.ImageField(blank=True,upload_to="media/")

    def __str__(self):
        return (self.namee)

class assign_book(models.Model):
    st=models.ForeignKey(student,on_delete=models.CASCADE)
    bt=models.ForeignKey(book,on_delete=models.CASCADE)
    due_date=models.DateField(null=True)
    idate=models.DateField(null=True)
    rdate=models.DateField(null=True,blank=True)
    fine=models.IntegerField()

    def __str__(self):
        return (self.st)

class purchase_book(models.Model):
    st=models.ForeignKey(student,on_delete=models.CASCADE)
    bt=models.ForeignKey(book,on_delete=models.CASCADE)
    price=models.IntegerField(null=True)
    purchase_date=models.DateField(null=True)
    stock_left=models.CharField(max_length=100)

    def __str__(self):
        return (self.st)

class student_attendance(models.Model):
    st=models.ForeignKey(student,on_delete=models.CASCADE)
    date=models.DateField()
    attendance=models.CharField(max_length=100,default="ABSENT")

    def __str__(self):
        return (self.st)

