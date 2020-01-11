from django.shortcuts import render
from productmanagement.models import Product, Phones, Accessories

# Create your views here.

def view_search(request):
    # allproduct=Product.objects.all()
    query= request.GET['query']
    allproduct=Product.objects.filter(name__icontains=query)
    para={'allproduct': allproduct}
    return render(request,'search.html', para)