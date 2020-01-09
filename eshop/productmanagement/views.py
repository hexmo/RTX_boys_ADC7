from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from django.views.generic import CreateView
from .models import Phones

# Create your views here.
def view_phone_form(request):
    return render(request,'addPhoneForm.htm')

#useful for form template
class PhoneCreateView(CreateView):
    model = Phones
    fields = ('brand','phoneModel','display','color','memory','battery','price')

#save retrieved data in database
def  save_in_database(request):

    get_brand = request.POST['Brand']
    get_phoneModel = request.POST['Model']
    get_display = request.POST['Display']
    get_color = request.POST['Color']
    get_battery = request.POST['Battery']
    get_memory = request.POST['Memory']
    get_price = request.POST['Price']
        
    phoneObj = Phones(brand=get_brand,phoneModel=get_phoneModel,display=get_display,color=get_color,battery=get_battery,price=get_price,memory=get_memory)
    phoneObj.save()

    return HttpResponse("Successful")
