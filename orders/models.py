from django.db import models


# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}, {self.email}, {self.first_name}, {self.last_name}"


class MenuItem(models.Model):
    TYPE_CHOICES = {
        ("pizza_regular", "Regular Pizza"),
        ("pizza_sicilian", "Sicilian Pizza"),
        ("toppings", "Toppings"),
        ("subs", "Subs"),
        ("pasta", "Pasta"),
        ("salads", "Salads"),
        ("dinner_platters", "Dinner Platters")
    }

    # SIZE_CHOICES = {
    #     ("small", "Small"),
    #     ("large", "Large")
    # }

    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    item = models.CharField(max_length=45)
    price_small = models.FloatField(null=True, blank=True)
    price_large = models.FloatField(null=True, blank=True)

    # size = models.CharField(max_length=10, choices=SIZE_CHOICES)

    def __self__(self):
        return f"({self.id}) {self.item} ${self.price_small / self.price_large} - {self.type}"


# class Topping(models.Model):
#     item = models.CharField(max_length=45)
#
#     def __self__(self):
#         return f"({self.id}) {self.item}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = models.FloatField()

    def __self__(self):
        return f"{self.id} - {self.client}: ${self.total}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.FloatField()

    def __self__(self):
        return f"{self.order}: ${self.price}"
