from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, default="None")
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Product(models.Model):
    # SIZE_CHOICES = {
    #     ("small", "Small"),
    #     ("large", "Large")
    # }

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    # size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=f"products/{slug}", blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', "slug"),)

    def __self__(self):
        return f"({self.id}) {self.name} ${self.price} - {self.category}"

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class Client(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.username}, {self.email}, {self.first_name}, {self.last_name}"


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
