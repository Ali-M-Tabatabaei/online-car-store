from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('add-to-cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('comment/<int:id>', views.comment, name="comment")
]
