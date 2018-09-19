from django.conf.urls import url

from orders_management import views

app_name = "orders_management"

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create')
]
