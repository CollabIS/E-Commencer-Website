from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username + ": " + self.user.email


class Product(models.Model):
    SIZE_CHOICES = [
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

    COLOR_CHOICES = [
        ("WHITE", "White"),
        ("BLACK", "Black"),
        ("MULTICOLOR", "Multicolor"),
        ("RED", "Red"),
        ("BROWN", "Brown"),
        ("BLUE", "Blue")
    ]

    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default="M")
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="WHITE")
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, default="T-SHIRT")
    image = models.ImageField(null=True, blank=True)
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    def getCategories(self):
        return [choice[0] for choice in self.CATEGORY_CHOICES]

    def getSizes(self):
        return [choice[0] for choice in self.SIZE_CHOICES]

    def getColors(self):
        return [choice[0] for choice in self.COLOR_CHOICES]

    def getPrice(self):
        return self.price


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    total_price = models.FloatField(default=0)

    def calculate_total_price(self):
        order_items = OrderItem.objects.filter(order=self)
        total_price = 0.0
        total_price = sum(item.product.price * item.quantity for item in order_items)
        self.total_price = total_price
        self.save()
        return total_price


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
