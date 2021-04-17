from django.db import models
from decimal import Decimal

class Bank(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length = 150)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Unit(models.Model):
    symbol = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.description

class Address(models.Model):
    city = models.CharField(max_length = 150)
    avenue = models.CharField(max_length = 255)
    village = models.CharField(max_length = 255)
    number = models.CharField(max_length = 150)
    
    
    def __str__(self):
        return self.number
    
class Client(models.Model):
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    website = models.CharField(max_length = 300, null=True, blank=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    website = models.CharField(max_length = 300, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Transporter(models.Model):
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    website = models.CharField(max_length = 300, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
       
    
class Product(models.Model):
    code = models.CharField(max_length = 150)
    bar_code = models.CharField(max_length = 255, null=True, blank=True)
    description = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=13, decimal_places=2, default=Decimal('0.00'))
    sell = models.DecimalField(max_digits=13, decimal_places=2, default=Decimal('0.00'))
    additional_info = models.CharField(max_length = 500, null=True, blank=True)
    minimum_stock = models.DecimalField(max_digits=13, decimal_places=2, default=Decimal('0.00'))
    actual_stock = models.DecimalField(max_digits=13, decimal_places=2, default=Decimal('0.00'))
    
    
    def __str__(self):
       return self.description

    
    
    
    
    
    
    
