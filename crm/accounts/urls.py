from django.http import HttpResponse
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.home, name="home"),
    path('product' , views.product,name="products"),
    path('register' , views.registerationPage,name="register"),
    path('login' , views.loginPage,name="login"),
    path('logout' , views.logoutUser,name="logout"),
    path('customer/<str:pk>/' , views.customer ,name="customer"),
    path('user' , views.userPage,name="user-page"),
    path('create_order/<str:pk>/' , views.createOrder , name = "create_order"),
    path('update_order/<str:pk>/' , views.updateOrder , name = "update_order"),
    path('delete_order/<str:pk>/' , views.deleteOrder , name = "delete_order"),


 ]
