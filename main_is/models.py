from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    size = models.CharField(max_length=100)
    quantity_available = models.IntegerField()


class Order(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    subtotal = models.FloatField()


class ShoppingBag(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)


class BagItems(models.Model):
    shop_bag_id = models.ForeignKey('ShoppingBag', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()


