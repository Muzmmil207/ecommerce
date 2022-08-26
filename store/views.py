from django.shortcuts import render, redirect
from .models import *
from .forms import ShippingAddressForm, CustmoerForm
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


def LoginView(request):

    if request.user.is_authenticated:
        return redirect('home')

    page = 'LoginView'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist.')

    return render(request, 'login_reqister.html', {'page': page})


def LogoutView(request):
    logout(request)
    return redirect('home')


def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'login_reqister.html', {'form': form})


@login_required(login_url="login-reqister/")
def home(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {}
        cartItem = ''

    context = {'products': products, 'order': order, 'cartItem': cartItem}
    return render(request, 'home.html', context)


@login_required(login_url="login-reqister/")
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {}
        cartItem = ''

    context = {'items': items, 'order': order, 'cartItem': cartItem}
    return render(request, 'cart.html', context)


@login_required(login_url="login-reqister/")
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_items
    else:
        items = []
        order = {}
        cartItem = ''

    form = ShippingAddressForm()
    form2 = CustmoerForm()
    context = {'items': items, 'order': order,
               'form': form, 'form2': form2, 'cartItem': cartItem}
    return render(request, 'checkout.html', context)


@login_required(login_url="login-reqister/")
def cart2(request):
    form = ShippingAddressForm()
    if request.method == 'POST':
        formData = ShippingAddressForm(request.POST)
        if formData.is_valid():
            formData.save()
    return render(request, 'cart2.html', {'form': form})


@login_required(login_url="login-reqister/")
def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print('productId', productId, action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, create = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, create = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('json respons', safe=False)


@login_required(login_url="login-reqister/")
def ProcessOrder(request):
    print('headers: ', request.headers)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                Country=data['shipping']['Country'],
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
            ShippingAddress.save()
    return JsonResponse('', safe=False)
