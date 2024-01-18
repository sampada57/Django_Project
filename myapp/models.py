from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

class Product(models.Model):
    name=models.CharField(max_length=200)  
    description=models.TextField() 
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class Customer(models.Model):
    name=models.CharField(max_length=200)  
    email=models.TextField() 
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    country=models.TextField(max_length=200)

class Order(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)  
    detail_info=models.ForeignKey(Customer,on_delete=models.CASCADE)
    


    
    