from django.db import models

class Pearson(models.Model):

    Name = models.CharField(max_length=150)
    Age = models.IntegerField()
    Email = models.EmailField(unique=True)
    Address = models.TextField()

    Created_Date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
