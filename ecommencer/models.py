from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.name + ": " + self.email


class Product(models.Model):
    Size_XL = "XL"
    Size_L = "L"
    Size_M = "M"
    Size_S = "S"
    Size_XS = "XS"
    SIZES_CHOICES = [
        (Size_XL, "Extra large"),
        (Size_L, "Large"),
        (Size_M, "Medium"),
        (Size_S, "Small"),
        (Size_XS, "Extra small")
    ]

    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    size = models.CharField(max_length=2, choices=SIZES_CHOICES, default=Size_M)
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name + " " + self.size


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

