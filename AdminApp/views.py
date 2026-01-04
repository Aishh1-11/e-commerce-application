from django.shortcuts import render,redirect
from AdminApp.models import CategoryDb,ProductDb
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def dashboard(request):

    product_no = ProductDb.objects.count()
    cat_no = CategoryDb.objects.count()
    return render(request,"dashboard.html",{"product_no":product_no,"cat_no":cat_no})

def add_category(request):
    return render(request,"add_category.html")

def save_category(request):

    if request.method=="POST":
        name = request.POST.get("name")
        des = request.POST.get("description")
        img = request.FILES.get("image")

        obj = CategoryDb(Name=name,Description=des,Image=img)
        obj.save()

    return redirect("add_category")

def display_categories(request):

    category_data = CategoryDb.objects.all()

    return render(request,"display_categories.html",{"category_data":category_data})

def edit_category(request,category_id):

    category = CategoryDb.objects.get(id=category_id)

    return render(request,"edit_category.html",{"category":category})

def update_category(request,category_id):
    category = CategoryDb.objects.get(id=category_id)

    if request.method == "POST":



        category.Name = request.POST.get("name")
        category.Description = request.POST.get("description")

        img = request.FILES.get("image")

        if img :

            category.Image = img

        category.save()



        return redirect(display_categories)


def delete_category(request,category_id):

    category = get_object_or_404(CategoryDb, id=category_id)

    if request.method == "POST":
        category.delete()
        return redirect(display_categories)

    return redirect(display_categories)

# ********************************************************************************************************************************

def add_product(request):

    categories = CategoryDb.objects.all()
    return render(request,"add_product.html",{"categories":categories})

def save_product(request):

    if request.method=="POST":

        category=request.POST.get("category")
        prdct = request.POST.get("product")
        price = request.POST.get("price")
        brand = request.POST.get("brand")
        short_des = request.POST.get("short-description")
        detailed_des = request.POST.get("detailed-description")
        image1 = request.FILES.get("image1")
        image2 = request.FILES.get("image2")
        image3 = request.FILES.get("image3")

        obj = ProductDb(CategoryName=category,Product=prdct,Price=price,Brand=brand,Short_description=short_des,Detailed_description=detailed_des,Image1=image1,Image2=image2,Image3=image3)
        obj.save()
    return redirect(add_product)


def display_products(request):

    products = ProductDb.objects.all()
    return render(request,'display_products.html',{"products":products})


def edit_product(request,product_id):

    product = ProductDb.objects.get(id=product_id)
    categories = CategoryDb.objects.all()
    return render(request,"edit_product.html",{"product":product,"categories":categories})

def update_product(request,product_id):

    product = ProductDb.objects.get(id=product_id)

    if request.method == "POST":

        product.CategoryName=request.POST.get("category")
        product.Product = request.POST.get("product")
        product.Brand = request.POST.get("brand")
        product.Price = request.POST.get("price")
        product.Short_description = request.POST.get("short-description")
        product.Detailed_description = request.POST.get("detailed-description")

        img1 = request.FILES.get("image1")
        if img1 :
            product.Image1 = img1

        img2 = request.FILES.get("image2")
        if img2 :
            product.Image2 = img2

        img3 = request.FILES.get("image3")
        if img3:
            product.Image3 = img3

        product.save()

        return redirect(display_products)

def delete_product(request,product_id):

    product = get_object_or_404(ProductDb,id=product_id)

    if request.method=="POST":

        product.delete()
        return redirect(display_products)

    return redirect(display_products)

#************************************************************************************************************************

def admin_login_page(request):
    return render(request,"admin_login_page.html")

def admin_login(request):

    if request.method == "POST":

        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        if User.objects.filter(username__contains = uname).exists():

            data = authenticate(username=uname,password=pwd)
            if data is not None :
                login(request,data)
                request.session['username']=uname
                request.session['password']=pwd
                return redirect(dashboard)

            else:
                return redirect(admin_login_page)

        else :
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)
