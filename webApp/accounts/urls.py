from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cancle-cart', views.cancle_cart, name='cancle_cart'),
    path('confirm-cart', views.confirm_cart, name='confirm_cart'),
    path('for-sale/<int:id>', views.for_sale, name='for_sale'),
    path('cancle-sale/<int:id>',  views.cancle_sale, name="cancle_sale"),
    path('cancle-from-cart/<int:id>',  views.cancle_from_cart, name="cancle_from_cart"),
    path('add_car', views.add_car, name="add_car"),
    path('delete_car/<int:id>', views.delete_car, name='delete_car'),
    path('update_car', views.update_car, name="update_car"),
]
