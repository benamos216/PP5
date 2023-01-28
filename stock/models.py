from django.db import models
import random


class Category(models.Model):
    """Category Model"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Stock(models.Model):
    """Stock Model"""

    """Generates unique sku for each product added"""
    def create_new_sku():
        not_unique = True
        while not_unique:
            unique_sku = random.randint(1000000000, 9999999999)
            if not Stock.objects.filter(sku=unique_sku):
                not_unique = False
        return str(unique_sku)

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True, editable=False, default=create_new_sku)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
