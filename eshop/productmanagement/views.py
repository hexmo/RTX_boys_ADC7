from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from django.views.generic import CreateView
from .models import Product
from .models import Phones

# Create your views here.
def view_phone_form(request):
    return render(request,'addPhoneForm.htm')

def view_product_form(request):
    return render(request,'productAddForm.htm')

def save_product_database(request):
    get_name = request.POST['Name']
    get_price = request.POST['Price']
    get_stockNo = request.POST['StockNo']
    get_releaseDate = request.POST['Date']
    get_specs = request.POST['Specification']
    # get_image = request.POST['Image']
    get_brand = request.POST['Brand']

    productObj = Product(name=get_name,price=get_price,stockNo=get_stockNo,releaseDate=get_releaseDate,specs=get_specs,brand=get_brand)
    productObj.save()
    return HttpResponse("Successful")




#save retrieved data in database
def  save_phone_database(request):

    get_screenSize = request.POST['screen size']
    get_RAM = request.POST['ram']
    get_ROM = request.POST['rom']
    get_color = request.POST['Color']
    get_battery = request.POST['Battery']
    get_description = request.POST['Description']
        
    phoneObj = Phones(screenSize=get_screenSize,RAM=get_RAM,ROM=get_ROM,color=get_color,battery=get_battery,description=get_description)
    phoneObj.save()

    return HttpResponse("Successful")
