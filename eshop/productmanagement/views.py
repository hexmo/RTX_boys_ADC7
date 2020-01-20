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

#this display the form to add phone
def view_phone_form(request):
    return render(request,'addPhoneForm.htm')

#this display the form for accessories
def view_accessories_form(request):
    return render(request,'accessoriesForm.htm')

# def view_phone_update(request):
#     if request.method=="POST":
#         get_id = request.POST
#         phoneObj=Phone.objects.get(id=get_id)
#         contxt_var={
#             "phone":phoneObj
#         }
#     else:    
#         return render(request, 'updateForms/phoneUpdate.htm', contxt_var)

#To get the inserted number and create context variable and pass to another form
def get_acc_id(request):
    access_id = request.GET['acc_id']
    # print(access_id)
    accObj = Accessories.objects.get(id=access_id)
    context={
        'acc':accObj
    }
    return render(request,'updateForms/accessoriesUpdate.htm',context)
#function to update the accessories
def update_accessories(request,id):
    name=request.POST['Name']
    brand=request.POST['Brand']
    price=request.POST['Price']
    stockNo=request.POST['StockNo']
    date=request.POST['Date']
    description = request.POST['Description']
    category = request.POST['Category']
# update queries
    updateAccessories = Accessories.objects.get(id=id)
    updateAccessories.name=name
    updateAccessories.brand=brand
    updateAccessories.price=price
    updateAccessories.stockNo=stockNo
    updateAccessories.date=date
    updateAccessories.description=description
    updateAccessories.category=category
    # if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
    #     image=request.FILES['Image']
    #     specs=request.FILES['Specification']
    #     fs2 = FileSystemStorage()
    #     filename = fs2.save(image.name, updateAccessories.image)
    #     uploaded_file_url2 = fs2.url(filename)
    #     filename2 = fs2.save(specs.name,updateAccessories.specs)
    #     uploaded_file_url2 = fs2.url(filename2)
    updateAccessories.save()
    return HttpResponse("Successfully Updated !!")


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

#save added accessories
def save_accessories(request):
    get_name = request.POST['Name']
    get_price = request.POST['Price']
    get_stockNo = request.POST['StockNo']
    get_releaseDate = request.POST['Date']
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




# *************************************************************************************
# All codes created below this section are done by Ranjan KC
def deleteProducts(request):
    phones = Phones.objects.all()
    accessories = Accessories.objects.all()
    params = {'products':phones}
    return render(request,'delete.html',params)

def confirmDeleteProducts(request,ID):
    product = Phones.objects.get(id=ID)
    product.delete()
    return HttpResponse("Successfully Deleted !!")
