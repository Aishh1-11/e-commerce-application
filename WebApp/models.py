from django.db import models

# Create your models here.

class UserDb(models.Model):
    User_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=255)


class ContactDb(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=200)
    Message = models.TextField(max_length =200)
