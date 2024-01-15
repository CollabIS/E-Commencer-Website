from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.models import Q

from ecommencer.models import *


# Create your views here.
def product_page(request, prod_name, prod_id):
    product_values = Product.objects.filter(id=prod_id).values()
    product = list(product_values).pop()

    product_sizes = Product().getSizes()
    product_colors = Product().getColors()
    product_categories = Product().getCategories()

    products_q_sizes = Product.objects.filter(name=prod_name).values('size').distinct()
    products_q_colors = Product.objects.filter(name=prod_name).values('color').distinct()

    print(products_q_sizes)

    context = {
        'product': product,

        'categories': product_categories,
        'available_sizes':  products_q_sizes,
        'available_colors': products_q_colors
    }
    return render(request, 'products/product.html', context)


def items_page(request, category):
    products = Product.objects.filter(category=category.upper())

    size_filter = request.POST.getlist('size')
    color_filter = request.POST.getlist('color')
    min_price_filter = request.POST.get('min_price')
    max_price_filter = request.POST.get('max_price')

    if size_filter:
        products = products.filter(size__in=size_filter)

    if color_filter:
        products = products.filter(color__in=color_filter)

    if min_price_filter:
        products = products.filter(price__gte=min_price_filter)

    if max_price_filter:
        products = products.filter(price__lte=max_price_filter)

    products_v = products.values()
    print(products_v)

    product_sizes = Product().getSizes()
    product_colors = Product().getColors()
    product_categories = Product().getCategories()
    filters = ["SIZE", "COLOR", "PRICE"]

    context = {
        'category': category,
        'products': products_v,

        'category_choices': product_categories,
        'size_choices': product_sizes,
        'color_choices': product_colors,

        'filters': filters,

        'selected_size_filter': size_filter,
        'selected_color_filter': color_filter,
        'selected_min_price_filter': min_price_filter,
        'selected_max_price_filter': max_price_filter,
    }

    return render(request, 'products/items_rows.html', context)


def home_page(request):
    context = {'category_choices': Product().getCategories()}
    return render(request, 'home/index.html', context)


def log_in_page(request):
    if request.user.is_authenticated:
        return render(request, 'account/user_info.html')

    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pass')

        current_customer = authenticate(request, username=username, password=password)

        if current_customer is not None:
            login(request, current_customer)
            return redirect('home-page')
        else:
            print("error login")
            return render(request, 'account/login.html')

    else:
        return render(request, 'account/login.html')


def sign_up_page(request):
    if request.user.is_authenticated:
        return render(request, 'account/user_info.html')

    if request.method == 'POST':
        username = request.POST.get('usr')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        new_customer = Customer(user=new_user)
        new_customer.save()

        return render(request, 'account/login.html')

    else:
        return render(request, 'account/signup.html')
