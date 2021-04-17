from django.db import models

from cadastro.models import Product

from decimal import Decimal


class StockedProduct(models.Model):
    locale = models.ForeignKey('StockLocale', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.DecimalField(max_digits=13, decimal_places=2, default=Decimal('0.00'))
    
    class Meta:
        verbose_name = 'Stocked Product'
        verbose_name_plural = 'Stocked products'
    
    def __str__(self):
        return self.product
    
class StockLocale(models.Model):
    description = models.CharField(max_length = 150)
    product_stock = models.ManyToManyField(Product, through='StockedProduct')
    
    class Meta:
        verbose_name = 'Stock Locale'
        verbose_name_plural = 'Stock Locales'
    
    def __str__(self):
        return self.description
    
    

