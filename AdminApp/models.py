from django.db import models

# Create your models here.

class  CategoryDb(models.Model):

    Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=400, null=True, blank=True)
    Image = models.ImageField(upload_to="category images",null=True,blank=True)

class ProductDb(models.Model):

    CategoryName = models.CharField(max_length=100,null=True,blank=True)
    Product = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Brand = models.CharField(null=True,blank=True)
    Short_description = models.CharField(max_length=300,null=True,blank=True)
    Detailed_description = models.CharField(max_length=500,null=True,blank=True)
    Image1 = models.ImageField(upload_to="Product images",null=True,blank=True)
    Image2 = models.ImageField(upload_to="Product images",null=True,blank=True)
    Image3 = models.ImageField(upload_to="Product images",null=True,blank=True)




