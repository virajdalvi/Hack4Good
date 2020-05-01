from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request,'login.html')


def login(request):
    if request.method == 'POST':

        user_name = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username = user_name,password = password1 )
            
        if user is not None : 
            auth.login(request,user)
            return render(request,'home.html')
        else :
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    
    else :
        return render(request,'login.html')
    


def home(request):
    return render(request,'register.html')
def register(request):

    user_name = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2 :
        if User.objects.filter(username=user_name).exists():
            messages.info(request,'Username taken, please re-enter the details.')
            return render(request,'register.html')

        else : 

            user = User.objects.create_user(username = user_name,password = password1)
            user.save()
            print(' User Saved!')
            return render(request,'login.html')
    
    else : 
        messages.info(request,'password doesnt match, re-enter the details. ')
        return render(request,'register.html')