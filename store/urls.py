from django.urls import path
from .views import index,login,signup



urlpatterns = [
    path('', index.index,name='index'),
    # path('signup' , signup,name='signup'),
    # path('login' , login,name='login')
    path('signup',signup.Signup.as_view(), name='signup'),
    path('login',login.Login.as_view(),name='login')
    
]