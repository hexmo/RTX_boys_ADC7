from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
# Create your views here.

# homepage
def homepage(request):
    return render(request,'viewproduct/home.html')


# def seePhones(request):
#     return render(request,'phones.html')

# def seeLaptops(request):
#     return render(request,'laptops.html')

# def seeAccessories(request):
#     return render(request,'accessories.html')
