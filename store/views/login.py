from django.shortcuts import render,redirect
from store .models.customer import Customer
from django import http
from django.contrib import messages
from django .views import View


class Login(View):
     def get(self, request):
      return render(request, 'store/login.html')
         
     def post(self, request):
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
        
        