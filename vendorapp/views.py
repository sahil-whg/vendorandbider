from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Vendor
# Create your views here.
def index(request):

    return render(request,'vendorapp/index.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_1 = request.POST['email_1']
        email_2= request.POST['email_2']
        password_1 = request.POST['password_1']
        password_2= request.POST['password_1']
        company_name = request.POST['company_name']
        address_1 = request.POST['address_1']
        address_2 = request.POST['address_2']
        mobile_no = request.POST['mobile_no']
        city = request.POST['city']
        postal = request.POST['postal']

        if password_1 == password_2:
            user = Vendor.objects.create_user(username="abc",password=password_1,email=email_1,first_name=first_name,last_name=last_name,company_name=company_name,mobile_number=mobile_no,address_1=address_1,address_2=address_2,city=city,zip=postal,is_staff=True,is_superuser=True)
            user.save()
            print("User Created")
        else:
            print("Password Mismatched")
            messages.info(request, "Password Mismatch")
        return redirect('vendorapp/index.html')
    else:
        return redirect('vendorapp/login.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'vendorapp/vendor_login.html')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, 'vendorapp/index.html')
    else:
        return render(request,'vendorapp/login.html')

def logout(request):

    auth.authenticate(request)
    return redirect('/')
