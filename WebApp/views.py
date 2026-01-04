from django.shortcuts import render,redirect
from AdminApp.models import *
from django.contrib.auth.hashers import make_password, check_password
from WebApp.models import *
# Create your views here.

def home(request):
    categories = CategoryDb.objects.all()
    product1 = ProductDb.objects.get(id=5)
    product2 = ProductDb.objects.get(id=11)
    return render(request,"home.html",{"categories":categories,"product1":product1,"product2":product2})

def products(request):
    products = ProductDb.objects.all()
    return render(request,"products.html",{"products":products})

def about(request):
    return render(request,"about.html")

def filtered_products(request,cat_name):
    products = ProductDb.objects.filter(CategoryName__iexact=cat_name.strip())
    return render(request, "filtered_products.html", {"products": products})

def single_product(request,prdct_id):
    product = ProductDb.objects.get(id=prdct_id)
    return render(request,"single_product.html",{"product":product})

def signin_signup(request):
    return render(request,"signin_signup.html")

def user_registration(request):

    if request.method == "POST":

        uname = request.POST.get("username")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        c_pwd = request.POST.get("confirm_password")

        if pwd != c_pwd:
            return redirect("signin_signup")


        hashed = make_password(pwd)

        UserDb.objects.create(User_name=uname,Email=email,Password=hashed)

    return redirect("signin_signup")

def user_login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            user = UserDb.objects.get(User_name=uname)
        except UserDb.DoesNotExist:
            return redirect("signin_signup")

        if check_password(pwd, user.Password):
            request.session["User_name"] = uname
            return redirect("home")

        return redirect("signin_signup")

    return redirect("signin_signup")








