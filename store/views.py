from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models.product import Product
from . models.category import Category
from . models.customer import Customer
from django import http
from django.contrib import messages
from .models import Customer





# Create your views here.

#index 
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
     products = Product.get_all_products_by_categoryid(categoryID)
    else:
       products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'store/index.html',data)

#signup
 
def signup(request):
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        postData = request.POST
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #vilidation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'mobile' : mobile,
            'email' : email,
        }
        
        error_message = None
        
        customer = Customer(first_name=first_name, last_name=last_name,
                             mobile_number=mobile, email=email,
                            password=password)
        
        if not first_name:
            error_message = "First Name is required"
        elif len(first_name) < 4:
            error_message = 'First Name must be 4 characters long or more'
        elif not last_name:
            error_message = 'Last Name is required'
        elif len(last_name) < 4:
            error_message = 'Last Name must be 4 characters long or more'
        elif not mobile:
            error_message = 'Mobile Number is required'
        elif len(mobile) < 11:
            error_message = 'Mobile Number must be 11 characters long'
        elif len(password) < 6:
            error_message = 'Password must be 6 characters long'
        elif len(email) < 5:
            error_message = 'Email must be 5 characters long'
        elif Customer.objects.filter(email=email).exists():
            error_message = 'Email Address Already Registered'
        
        if not error_message:
            customer = Customer(first_name=first_name, last_name=last_name,
                                mobile_number=mobile, email=email, password=password)
        if not error_message:
            customer.register()
            messages.success(request, 'Your account has been created successfully')
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
    return render(request, 'store/signup.html',data)


#login 

def login(request):
    if request.method == 'GET':
     return render(request, 'store/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email=email)
        error_message = None
        if customer:
            flag = check_password = (password)
            if flag:
                messages.success(request,'you have been logged in successfully!!!')
                return redirect('index')
            else:
              error_message = 'Email or Password invalid !!!'
                
        else:
            error_message = 'Email or Password invalid !!!'
            return render(request, 'store/login.html',{'error':error_message})
        
        
        

