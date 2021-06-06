from django.db import models

# Create your models here.

 

class Doctor(models.Model):
    query=models.TextField(null=True)    

    def __str__(self): 
            return self.Doctor.query
