from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cancle-cart', views.cancle_cart, name='cancle_cart'),
    path('confirm-cart', views.confirm_cart, name='confirm_cart')
]
