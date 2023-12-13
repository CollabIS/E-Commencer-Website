from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username + ": " + self.user.email


class Product(models.Model):

    SIZES_CHOICES = [
        ("XL", "Extra large"),
        ("L", "Large"),
        ("M", "Medium"),
        ("S", "Small"),
        ("XS", "Extra small")
    ]

    CATEGORY_CHOICES = [
        ("T-SHIRT", "T-Shirt"),
        ("JACKET", "Jacket"),
        ("SWEATSHIRT", "Sweatshirt"),
        ("PANTS", "Pants"),
        ("ACCESSORIES", "Accessories")

    ]

    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    size = models.CharField(max_length=2, choices=SIZES_CHOICES, default="M")
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, default="T-SHIRT")
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name + " " + self.size

    def getCategories(self):
        return [choice[0] for choice in self.CATEGORY_CHOICES]



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

