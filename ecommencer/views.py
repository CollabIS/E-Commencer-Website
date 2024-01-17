from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db import IntegrityError

from ecommencer.models import *


# Create your views here.
def product_page(request, prod_name, prod_id):
    product_values = Product.objects.filter(id=prod_id).values()
    product = list(product_values).pop()

    product_categories = Product().getCategories()

    products_q_sizes = Product.objects.filter(name=prod_name).values('size').distinct()
    products_q_colors = Product.objects.filter(name=prod_name).values('color').distinct()

    context = {
        'product': product,

        'category_choices': Product().getCategories(),
        'categories': product_categories,
        'available_sizes': products_q_sizes,
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
    log_user = request.user.is_authenticated

    context = {'category_choices': Product().getCategories(),
               'authenticated': log_user}

    return render(request, 'home/index.html', context)


def log_in_page(request):
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pass')

        current_customer = authenticate(request, username=username, password=password)
        existing_customer = current_customer is not None
        context = {
            'existing_customer': existing_customer
        }

        if current_customer is not None:
            login(request, current_customer)
            return redirect('home-page')
        else:
            return render(request, 'account/login.html', context)

    else:
        context = {'existing_customer': True}
        return render(request, 'account/login.html', context)

def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST.get('usr')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            # Try to create a new user
            new_user, created = User.objects.get_or_create(username=username, email=email, password=password)

            # Check if the user was created (not already existing)
            if created:
                new_customer = Customer(user=new_user)
                new_customer.save()

                return render(request, 'account/login.html')
            else:
                # Handle the case when the user already exists
                return render(request, 'account/signup.html', {'error_message': 'User already exists'})

        except IntegrityError:
            # Handle IntegrityError (e.g., duplicate key violation)
            return render(request, 'account/signup.html', {'error_message': 'Error creating user'})

    else:
        return render(request, 'account/signup.html')


def user_account(request):
    user = request.user
    customer = Customer.objects.filter(user=user).first()
    orders = Order.objects.filter(customer=customer)
    order_items = list()
    for order in orders:
        order_items.append((order, OrderItem.objects.filter(order=order)))
        print(order.calculate_total_price())

    context = {
        'category_choices': Product().getCategories(),
        'username': str(user).upper,
        'orders': order_items
    }

    if request.method == "POST":
        logout(request)
        return redirect('home-page')
    return render(request, 'account/user_info.html', context)
