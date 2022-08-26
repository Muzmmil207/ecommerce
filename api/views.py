from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, Order, OrderItem, ShippingAddress
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import ProductSerializer, OrderSerializer, OrderItemSerializer, ShippingAddressSerializer
# Create your views here.


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes = [
        'GET ',
        'GET /products',
        'GET /products/<str:pk>',
        'GET /orders',
        'GET /orders/<str:pk>',
        'GET /order-items',
        'GET /order-items/<str:pk>',
        'GET /shipping-addreses',
        'GET /shipping-addreses/<str:pk>',
    ]
    return Response(routes)

# this Product model api


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def ProductsApi(request):

    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)

    if request.method == 'GET':
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def ProductApi(request, pk):

    try:
        product = Product.objects.get(id=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        product.delete()
        return Response(serializer.data)

# this Order model api


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def OrdersApi(request):

    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)

    if request.method == 'GET':
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def OrderApi(request, pk):

    try:
        order = Order.objects.get(id=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        order.delete()
        return Response(serializer.data)

# this OrderItem model api


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def OrderItemsApi(request):

    order_item = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_item, many=True)

    if request.method == 'GET':
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def OrderItemApi(request, pk):

    try:
        order_item = OrderItem.objects.get(id=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderItemSerializer(order_item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        order_item.delete()
        return Response(serializer.data)

# this ShippingAddress model api


@api_view(['GET', 'POST'])
def ShippingAddresesApi(request):

    shipping_address = ShippingAddress.objects.all()
    serializer = ShippingAddressSerializer(shipping_address, many=True)

    if request.method == 'GET':
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ShippingAddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def ShippingAddressApi(request, pk):

    try:
        shipping_address = ShippingAddress.objects.get(id=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShippingAddressSerializer(shipping_address)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShippingAddressSerializer(
            shipping_address, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        shipping_address.delete()
        return Response(serializer.data)
