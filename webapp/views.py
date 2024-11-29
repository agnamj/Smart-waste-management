from django.shortcuts import render,redirect
from webapp.models import contact_Db,signup_db,cart_db,order_db
from Adonaiapp.models import category_DB,product_DB
from django.contrib import messages
import razorpay
def homepage(request):
    categories = category_DB.objects.all()
    return render(request,"home.html",{'categories':categories})
def about_page(request):
    return render(request,"About.html")
def checkout(request):
    return render(request,"checkout.html")
def contact_page(request):
    return render(request,"contact.html")
def save_contact(request):
    if request.method == "POST":
        a = request.POST.get('nname')
        b = request.POST.get('lName')
        c = request.POST.get('email')
        d = request.POST.get('mobile')
        e = request.POST.get('mess')
        obj = contact_Db(name=a, lname=b, email=c, mobile=d, message=e)
        obj.save()
        messages.success("User contact is saved......!")
        return redirect(contact_page)
def product_page(request):
    products = product_DB.objects.all()
    return render(request,"products.html", {'products':products})
def products_filtered(request,cat_name):
    data = product_DB.objects.filter(category_name=cat_name)
    return render(request,"product_filtered.html",{'data':data})
def single_product(request,single_id):
    single = product_DB.objects.get(id=single_id)
    return render(request,"single_Product.html",{'single':single})
def sign_up(request):
    return render(request,"signup.html")
def save_signup(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('pass')
        d = request.POST.get('re_pass')
        obj = signup_db(name=a, email=b, password=c, cpassword=d)
        obj.save()
        messages.warning(request, "User already exists...!")
        return redirect(sign_up)

def sign_in(request):
    return render(request,"signin.html")
def user_login(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pswd = request.POST.get('pass')
        if signup_db.objects.filter(name=un,password=pswd).exists():
            request.session['name']=un
            request.session['password']=pswd
            messages.success(request,"welcome...!")
            return redirect(homepage)
        else:
            messages.warning(request,"invalid username ")
            return redirect(sign_in)
    else:
        messages.error(request,"invalid password")
        return redirect(sign_in)

def user_logout(request):
    del request.session['name']
    del request.session['password']
    messages.warning(request, "username loggedout....!")
    return redirect(homepage)

def save_cart(request):
    if request.method == "POST":
        usern = request.POST.get('una')
        pn = request.POST.get('prodname')
        quan = request.POST.get('quantity')
        pri = request.POST.get('prp')
        top = request.POST.get('tp')
        obj = cart_db(username=usern, productname=pn, quantity=quan, price=pri,totalprice=top)
        obj.save()
        return redirect(homepage)

def cart_page(request):
    cart_data = cart_db.objects.filter(username=request.session['name'])
    subtotal = 0
    shipping = 0
    Total = 0
    for i in cart_data:
        subtotal = subtotal + i.totalprice
        if subtotal>50000:
            shipping = 100
        else:
            shipping = 250
        Total = shipping+subtotal
    return render(request,"cart.html",{'cart_data':cart_data,'subtotal':subtotal,'shipping':shipping,'Total':Total})
def delete_cart(request,car_id):
    y = cart_db.objects.filter(id=car_id)
    y.delete()
    messages.error(request, "product deleted ....!")
    return redirect(cart_page)
def checkout(request):
    check = cart_db.objects.filter(username=request.session['name'])
    subtotal = 0
    shipping = 0
    Total = 0
    for i in check:
        subtotal = subtotal + i.totalprice
        if subtotal > 50000:
            shipping = 100
        else:
            shipping = 250
        Total = shipping + subtotal
    return render(request,"checkout.html",{'check':check,'subtotal':subtotal,'shipping':shipping,'Total':Total,})
def save_check(request):
    if request.method =="POST":
        a = request.POST.get('name')
        b = request.POST.get('mail')
        c = request.POST.get('phon')
        d = request.POST.get('place')
        e = request.POST.get('address')
        f = request.POST.get('c_pin')
        g = request.POST.get('tprice')
        h = request.POST.get('message')
        obj = order_db(Name=a,Email=b,mobile=c,place=d,Address=e,pin=f,Totalprice=g,Message=h)
        obj.save()
        return redirect(payment_page)

def payment_page(request):
    customer = order_db.objects.order_by('-id').first()
    payy = customer.Totalprice
    amount = int(payy*100)
    payy_str = str(amount)
    for i in payy_str:
        print(i)
    if request.method=="POST":
        order_currency = 'INR'
        client = razorpay.Client(auth =('rzp_test_T8LJkDEUaCLwQB','MwdxR1VUjvVkV7SrF1Asbvfh'))
        payment = client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})