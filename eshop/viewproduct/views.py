from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
# Create your views here.
def seePhones(request):
    return render(request,'phones.htm')

def seeLaptops(request):
    return render(request,'laptops.htm')

def seeAccessories(request):
    return render(request,'accessories.htm')
