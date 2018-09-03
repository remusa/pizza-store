from django.contrib import admin
from orders.models import Client, MenuItem, Order, OrderDetail

# Register your models here.

admin.site.register(Client)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderDetail)
