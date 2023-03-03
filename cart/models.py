from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255
    )
    review = models.ManyToManyField("Cart")
    price = models.IntegerField()


class Cart(models.Model):
    review = models.TextField()
