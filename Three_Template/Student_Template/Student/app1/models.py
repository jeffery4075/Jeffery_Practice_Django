from django.db import models

class Student(models.Model):
    
    #personal info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.Choices()
    email = models.EmailField(max_length=120,unique=True)



