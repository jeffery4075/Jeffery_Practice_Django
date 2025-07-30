from django.db import models

class Profile_Details(models.Model):
    Name  = models.CharField(max_length=150)
    Email = models.EmailField(max_length=120)
    city =  models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)


    def __str__(self):
        return f"{self.Name} ({self.Email})"
    
class student_Details(models.Model):
    stu_class = models.CharField(max_length=120)
    marks = models.IntegerField()

    def __str__(self):
        return self.stu_class