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
    return render(request, 'login_signup_template/login.html')


def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST['usr']
        email = request.POST['email']
        password = request.POST['pass']

        user = User.objects.create_user(username, email, password)
        user.save()
        customer = Customer(user)
        customer.save()

    else:
        return render(request, 'login_signup_template/signup.html')