from django.shortcuts import render,redirect
from .models import Stockinfo
from django.http import HttpResponse
def stockav(request):
    return render(request,'stockav.html')
def home(request):
    return render(request,'home.html')
def submit(request):
    vendor_name=request.POST["vendor_name"],
    product_name=request.POST["product_name"],
    category=request.POST["category"],
    quantity=request.POST["quantity"],
    rate=request.POST["rate"],
    stockinfo=Stockinfo(vendor_name=vendor_name,product_name=product_name,category=category,quantity=quantity,rate=rate)
    stockinfo.save()
    return render(request,'home.html')
# Create your views here.
