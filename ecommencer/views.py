from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from ecommencer.models import *


# Create your views here.

def items_page(request, category):
    products = Product.objects.filter(category=category.upper())
    context = {'category': category, 'products': products, 'category_choices': Product().getCategories()}
    return render(request, 'items_template/items_template.html', context)


def product_page(request):
    pass


def home_page(request):
    context = {'category_choices': Product().getCategories()}
    return render(request, 'home_template/home_template.html', context)


def log_in_page(request):
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pass')

        current_customer = authenticate(request, username=username, password=password)

        if current_customer is not None:
            login(request, current_customer)
            return redirect('home-page')
        else:
            print("error login")
            return render(request, 'login_signup_template/login.html')

    else:
        return render(request, 'login_signup_template/login.html')


def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST.get('usr')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        new_customer = Customer(user=new_user)
        new_customer.save()

        return render(request, 'login_signup_template/login.html')

    else:
        return render(request, 'login_signup_template/signup.html')