from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from cars.models import Car
from . models import *
from django.core.files import File

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url = 'login')
def dashboard(request):
    user_cars = Own.objects.filter(user_id=request.user.id)
    own = []
    for i in user_cars:
        own.append(i.car)
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)

    user_purchased_cars = Purchased.objects.filter(user_id=request.user.id)

    cart = Cart.objects.filter(user_id = request.user.id)
    total_price = 0
    cart_cars = []
    for i in cart:
        cart_cars.append(i.car)
        total_price += i.car.price

    forSale = ForSale.objects.filter(user_id=request.user.id)
    cars_for_sale = []

    for i in forSale:
        cars_for_sale.append(i.car)

    sold = Sold.objects.filter(user_id=request.user.id)
    sold_cars = []
    for i in sold:
        sold_cars.append(i.car)

    data = {
        'user':request.user,
        'inquiries': user_inquiry,
        'cars': own,
        'cars1': user_purchased_cars,
        'cart_cars':cart_cars,
        'total_price':total_price,
        'cars_for_sale': cars_for_sale,
        'sold': sold_cars
    }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

def cancle_cart(request):
    Cart.objects.filter(user_id=request.user.id).delete()
    return redirect('dashboard')


def confirm_cart(request):
    cart = Cart.objects.filter(user_id = request.user.id)

    for i in cart:
        seler = ForSale.objects.get(car_id=i.car.id)
        sold = Sold()
        sold.user = seler.user
        sold.car = seler.car
        sold.save()
        seler.delete()
        Own.objects.filter(car_id=i.car.id).delete()
        o = Own()
        o.user = i.user
        o.car = i.car
        o.save()
        p = Purchased()
        p.user = i.user
        p.car = i.car
        p.save()
    
    cart.delete()
    return redirect('dashboard')


def for_sale(request, id):
    user = request.user
    car = Car.objects.get(id=id)
    forSale = ForSale()
    forSale.user = user
    forSale.car = car
    forSale.save()
    return redirect("dashboard")

def cancle_sale(request, id):
    ForSale.objects.get(car_id=id).delete()
    return redirect("dashboard")


def cancle_from_cart(request, id):
    Cart.objects.get(car_id=id).delete()
    return redirect("dashboard")


def add_car(request):
    car = Car()
    car.car_title = request.POST['car_title']
    car.city = request.POST['city']
    car.color = request.POST['color']
    car.price = request.POST['price']
    image = request.FILES['img']
    # print(image.name, "*****************")
    car.car_photo.save(image.name, image)
    car.engine = request.POST['engine']
    # print(request.POST['miles'], "*************")
    car.miles = int(request.POST['miles'])

    car.fuel_type = request.POST['fuel_type']
    car.save()

    o = Own()
    o.user = request.user
    o.car = car
    o.save()
    return redirect('dashboard')