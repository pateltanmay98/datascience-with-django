from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Purchase(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Solled {} - {} for {}".format(self.product.name, self.quantity, self.price)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super(Purchase, self).save(*args, **kwargs)
