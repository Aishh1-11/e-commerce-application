from django.urls import path
from WebApp import views

urlpatterns = [

    path("home/",views.home,name="home"),
    path("products/",views.products,name="products"),
    path("about/",views.about,name="about"),
    path("filtered_products/<cat_name>/",views.filtered_products,name="filtered_products"),
    path("single_product/<int:prdct_id>/",views.single_product,name="single_product"),

    path("signin_signup/",views.signin_signup,name="signin_signup"),
    path("user_registration/",views.user_registration,name="user_registration"),
    path("user_login/",views.user_login,name="user_login"),
]