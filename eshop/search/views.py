from django.shortcuts import render
from django.template import Template,context
from productmanagement.models import Phones,Accessories
# Create your views here.

def view_search(request):
    query=request.GET['query']
    if len(query)>78:
        phones=[]
    else:    
        phones= Phones.objects.filter(name__icontains=query)
    context_variable={'products': phones, 'query': query}
    return render(request,'search.html',context_variable)


def view_product(request,ID):
    product = Phones.objects.get(id=ID)
    context_varible = {'product':product}
    return render(request,'view2.html',context_varible)

