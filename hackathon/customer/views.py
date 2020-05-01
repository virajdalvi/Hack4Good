from django.shortcuts import render
from django.http import HttpResponse
from .models import Info
from .models import Product

# Create your views here.
def reg(request):
    return render(request,'reg.html')

def submit(request):
    c=request.POST["customer_name"]
    a=request.POST["address"]
    no=request.POST["contact_no"]
    gno=request.POST["Gst_no"]
    e=request.POST["Email_Id"]

    info=Info(customer_name=c,address=a,contact_no=no,Gst_no=gno,Email_Id=e)
    info.save()
    return render(request,"reg.html")

def buy(request):
    return render(request,'buy.html')

def click(request):
    
    p=request.POST["vendor_name"]
    q=request.POST["phone_no"]
    r=request.POST["Email"]
    s=request.POST["GST_no"]
    t=request.POST["product_name"]
    u=request.POST["quantity"]
    v=request.POST["GST_rate"]
    w=request.POST["price"]
    
    product=Product(vendor_name=p,phone_no=q,Email=r,GST_no=s,product_name=t,quantity=u,GST_rate=v,price=w)
    product.save()
    return render(request,"buy.html")



