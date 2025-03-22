from django.db import models
from django.utils import timezone

# Create your models here.

# Model for Supplier
class Supplier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def getName(self):
        return self.name
        
    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"

# Model for Water Bottle
class WaterBottle(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=50, decimal_places=2)
    size = models.CharField(max_length=50)
    mouth_size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_qty = models.IntegerField()
    objects = models.Manager()
        
    def __str__(self):
        return f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by}, {self.cost:.2f} : {self.current_qty}"