from django.shortcuts import render,redirect
from store .models.customer import Customer
from django import http
from django.contrib import messages
from django .views import View





class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')
       
    def post(self, request):
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
