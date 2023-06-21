from django.urls import path
from .views import index,login,signup,cart,checkout
from.views.login import logout
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware






urlpatterns = [
    path('', index.Index.as_view(),name='index'),
    # path('signup' , signup,name='signup'),
    # path('login' , login,name='login')
    path('signup',signup.Signup.as_view(), name='signup'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart', auth_middleware(cart.Cart.as_view()) , name='cart'),
    path('check-out',checkout.CheckOut.as_view(),name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),


    
    
    
]