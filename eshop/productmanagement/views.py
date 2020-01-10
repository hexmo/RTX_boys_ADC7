from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Template,context
from .models import Product
from .models import Phones
from .models import Accessories
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def view_manage_page(request):
    return render(request,'manageProduct.htm')

def view_phone_form(request):
    return render(request,'addPhoneForm.htm')

def view_accessories_form(request):
    return render(request,'accessoriesForm.htm')

# def save_product_database(request):
#     get_name = request.POST['Name']
#     get_price = request.POST['Price']
#     get_stockNo = request.POST['StockNo']
#     get_releaseDate = request.POST['Date']
#     get_specs = request.POST['Specification']
#     # get_image = request.POST['Image']
#     get_brand = request.POST['Brand']

#     productObj = Product(name=get_name,price=get_price,stockNo=get_stockNo,releaseDate=get_releaseDate,specs=get_specs,brand=get_brand)
#     productObj.save()
#     return HttpResponse("Successful")




#save retrieved data in database
def  save_phone_database(request):

    get_screenSize = request.POST['screen size']
    get_RAM = request.POST['ram']
    get_ROM = request.POST['rom']
    get_color = request.POST['Color']
    get_battery = request.POST['Battery']
    get_description = request.POST['Description']
    get_name = request.POST['Name']
    get_price = request.POST['Price']
    get_stockNo = request.POST['StockNo']
    get_releaseDate = request.POST['Date']
    #get_specs = request.FILES['Specification']
    #get_image = request.FILES['Image']
    get_brand = request.POST['Brand']
        
    
    if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
        image=request.FILES['Image']
        specs=request.FILES['Specification']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        filename2 = fs.save(specs.name,specs)
        uploaded_file_url = fs.url(filename2)

    phoneObj = Phones(image=uploaded_file_url,specs=uploaded_file_url,screenSize=get_screenSize,RAM=get_RAM,ROM=get_ROM,color=get_color,battery=get_battery,description=get_description,name=get_name,price=get_price,stockNo=get_stockNo,releaseDate=get_releaseDate,brand=get_brand)
    phoneObj.save()
    return HttpResponse("Successfully Stored !!")

def save_accessories(request):
    get_name = request.POST['Name']
    get_price = request.POST['Price']
    get_stockNo = request.POST['StockNo']
    get_releaseDate = request.POST['Date']
    # get_specs = request.POST['Specification']
    # get_image = request.FILES['Image']
    get_brand = request.POST['Brand']
    get_description = request.POST['Description']
    get_category = request.POST['Category']

    if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
        image=request.FILES['Image']
        specs=request.FILES['Specification']
        fs2 = FileSystemStorage()
        filename = fs2.save(image.name, image)
        uploaded_file_url2 = fs2.url(filename)
        filename2 = fs2.save(specs.name,specs)
        uploaded_file_url2 = fs2.url(filename2)

    accessoriesObj = Accessories(description=get_description,name=get_name,price=get_price,stockNo=get_stockNo,releaseDate=get_releaseDate,brand=get_brand,category=get_category,image=uploaded_file_url2,specs=uploaded_file_url2)
    accessoriesObj.save()
    return HttpResponse("Successfully Stored !!")