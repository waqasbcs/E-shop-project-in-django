from django.shortcuts import render, redirect,HttpResponseRedirect
from store.models.customer import Customer
from django import http
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import check_password

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'store/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email=email)
        error_message = None
        if customer:
            flag = check_password = (password)
            if flag:
                request.session['customer'] = customer.id
                messages.success(request,'you have been logged in successfully!!!')
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('index')
            else:
              error_message = 'Email or Password invalid !!!'
                
        else:
            error_message = 'Email or Password invalid !!!'
            return render(request, 'store/login.html',{'error':error_message})
        
def logout(request):
    request.session.clear()
    return redirect('login')
        
        