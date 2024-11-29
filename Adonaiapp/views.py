from django.shortcuts import render,redirect
from Adonaiapp.models import category_DB,product_DB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import contact_Db
from django.contrib import messages
import datetime

def index(request):
    date = datetime.datetime.now()
    return render(request,"index.html",{'date':date})
def add_category(request):
    return render(request,"Add_category.html")
def save_date(request):
    if request.method =="POST":
        a = request.POST.get('cname')
        b = request.POST.get('desc')
        c = request.FILES['image']
        obj = category_DB(category_name1=a,Description=b,category_img=c)
        obj.save()
        messages.success(request,"category saved succesfully......!")
        return redirect(add_category)
def display_category(request):
    cat = category_DB.objects.all()
    return render(request,"display_category.html",{'cat':cat})
def edit_category(request,cat_id):
    cat = category_DB.objects.get(id=cat_id)
    messages.success(request, "category edited successfully....!")
    return render(request,"edit_category.html",{'cat':cat})
def update_category(request,cat_id):
    if request.method =="POST":
        a = request.POST.get('cname')
        b = request.POST.get('desc')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = category_DB.objects.get(id=cat_id).category_img
        category_DB.objects.filter(id=cat_id).update(category_name1=a,Description=b,category_img=file)
        return redirect(display_category)

def delete_category(request,cat_id):
    x = category_DB.objects.filter(id=cat_id)
    x.delete()
    messages.error(request, "category deleted successfully....!")
    return redirect(display_category)

def product(request):
    cat = category_DB.objects.all()
    return render(request,"Add_products.html", {'cat':cat})

def save_pro(request):
    if request.method == "POST":
        a = request.POST.get('cname')
        b = request.POST.get('pname')
        c = request.POST.get('Quantity')
        d = request.POST.get('MRP')
        e = request.POST.get('desc')
        f = request.POST.get('coun')
        g = request.POST.get('manu')
        h = request.FILES['image1']
        i = request.FILES['image2']
        j = request.FILES['image3']
        obj = product_DB(category_name=a,pro_name=b,Quantity=c,Mrp=d,Description=e,country=f,manufactured=g,category_image1=h,category_image2=i,category_image3=j)
        obj.save()
        messages.error(request, "product deleted successfully....!")
        return redirect(product)
def display_product(request):
    pro = product_DB.objects.all()
    return render(request,"display_product.html",{'pro':pro})
def edit_product(request,pro_id):
    cat = category_DB.objects.all()
    pro = product_DB.objects.get(id=pro_id)
    messages.error(request, "product deleted successfully....!")
    return render(request,"edit_product.html",{'cat':cat,'pro':pro})

def update_product(request,pro_id):
    if request.method == "POST":
        a = request.POST.get('cname')
        b = request.POST.get('pname')
        c = request.POST.get('Quantity')
        d = request.POST.get('MRP')
        e = request.POST.get('desc')
        f = request.POST.get('coun')
        g = request.POST.get('manu')
        try:
            img = request.FILES['image1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file1 = product_DB.objects.get(id=pro_id).category_image1


        try:
            img2 = request.FILES['image2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2 = product_DB.objects.get(id=pro_id).category_image2


        try:
            img3 = request.FILES['image3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name,img3)
        except MultiValueDictKeyError:
            file3 = product_DB.objects.get(id=pro_id).category_image3
        product_DB.objects.filter(id=pro_id).update(category_name=a,pro_name=b,Quantity=c,Mrp=d,Description=e,country=f,manufactured=g,category_image1=file1,category_image2=file2,category_image3=file3)
        return redirect(display_product)

def delete_product(request,pro_id):
    y = product_DB.objects.filter(id=pro_id)
    y.delete()
    messages.error(request, "product deleted successfully....!")
    return redirect(display_product)
def loginpage(request):
    return render(request,"loginpage.html")
def admin_page(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pswd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request,"Welcome...!")
                return redirect(index)
            else:
                messages.warning(request,"please check your  password...!")
                return redirect(loginpage)
    else:
        messages.warning(request, "invalid username ...!")
        return redirect(loginpage)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def display_contact(request):
    con = contact_Db.objects.all()
    return render(request,"contact_data.html", {'con':con})
def delete_contact(request,con_id):
    x = contact_Db.objects.filter(id=con_id)
    x.delete()
    return redirect(display_contact)

