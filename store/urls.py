from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('cart2/', views.cart2, name="cart2"),
    path('checkout/', views.checkout, name="checkout"),

    path('login-reqister/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('register/', views.RegisterView, name="RegisterView"),

    path('update-item/', views.UpdateItem),
    path('process-order/', views.ProcessOrder),
]
