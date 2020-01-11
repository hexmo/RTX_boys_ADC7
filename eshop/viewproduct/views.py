from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from productmanagement.models import Phones,Accessories
# Create your views here.

# homepage
def homepage(request):
    phones = Phones.objects.all()
    accessories = Accessories.objects.all()
    # print(phones)
    # print(accessories)
    params = {'products':phones}
    return render(request,'viewproduct/home.html',params)

# displaying specific product
def viewProductDetails(request,ID):
    product = Phones.objects.get(id=ID)
    context_varible = {'product':product}
    return render(request,'viewproduct/view.html',context_varible)


# def seePhones(request):
#     return render(request,'phones.html')

# def seeLaptops(request):
#     return render(request,'laptops.html')

# def seeAccessories(request):
#     return render(request,'accessories.html')
