import imp
from django.urls import path
from .views import getRoutes, ProductsApi, ProductApi, OrdersApi, OrderApi, OrderItemsApi, OrderItemApi, ShippingAddresesApi, ShippingAddressApi


urlpatterns = [
    path('', getRoutes),
    path('products/', ProductsApi),
    path('products/<str:pk>', ProductApi),
    path('orders/', OrdersApi),
    path('orders/<str:pk>', OrderApi),
    path('order-items/', OrderItemsApi),
    path('order-items/<str:pk>', OrderItemApi),
    path('shipping-addreses/', ShippingAddresesApi),
    path('shipping-addreses/<str:pk>', ShippingAddressApi),
]
