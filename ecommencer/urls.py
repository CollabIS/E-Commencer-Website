from django.urls import path
from ecommencer import views


urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('login/', views.log_in_page, name="login-page"),
    path('signup/', views.sign_up_page, name="signup-page"),
    path('<str:category>/', views.items_page, name="items-page"),
    path('products/<str:prod_name><int:prod_id>/', views.product_page, name="product-page"),
]
