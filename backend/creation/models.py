from django.db import models

# Create your models here.
class UserRegister(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
class Loan(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    ammount = models.FloatField(max_length=12)
    
    