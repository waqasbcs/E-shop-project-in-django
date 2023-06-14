from django.shortcuts import render
from . models.product import Product
from . models.category import Category


# Create your views here.
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
 
# signup form
def signup(request):
   return render(request, 'store/signup.html')
