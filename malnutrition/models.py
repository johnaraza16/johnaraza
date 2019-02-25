from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname= models.CharField(max_length=100, help_text="Enter Your Firstname")
    lastname= models.CharField(max_length=100, help_text="Enter Your Lastname")
    birthdate= models.DateField(max_length=100)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    weight= models.DecimalField(decimal_places=2,max_digits=20, help_text="Enter your weight by kg")
    height= models.DecimalField(decimal_places=2,max_digits=20, help_text="Enter your height by cm")
    physical_activity=models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self): 
        return self.firstname + '-' + self.lastname
    

class Food(models.Model):
    calories= models.DecimalField(decimal_places=2,max_digits=20)
    fats= models.DecimalField(decimal_places=2,max_digits=20)
    foodname= models.CharField(max_length=100)
    images= models.ImageField(upload_to = 'media/Images', null=True, blank=True)
    description= models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self): 
        return self.foodname 

class Foodlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    Description= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    birthdate= models.DateField(max_length=100)
    gender= models.CharField(max_length=100)
    weight= models.DecimalField(decimal_places=2,max_digits=20)
    height= models.DecimalField(decimal_places=2,max_digits=20)

    def __str__(self): 
        return self.firstname

class Question(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    Questions = models.CharField(max_length=500)

    def __str__(self): 
        return self.Questions

class WeightTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight= models.DecimalField(decimal_places=2,max_digits=20)
    date = models.DateTimeField(auto_now_add=True, null=True, blank= True)

    def __str__(self): 
        return self.weight

