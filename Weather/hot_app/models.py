from django.db import models

# Create your models here.
class Register(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstname