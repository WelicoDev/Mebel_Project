from django.shortcuts import render , redirect
from django.contrib.auth import logout , login , authenticate
from .models import *
# Create your views here.

def SignUp(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        rep_password = request.POST.get('rep_password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        if password != rep_password:
            context = {
                "error_password" :True
            }
            return render(request,'register/register.html' , context)

        user = User.objects.filter(username=username).first()
        if user :
            context ={
                "error_user": True
            }
            return render(request,'register/register.html' , context)

        root = User()
        root.name = name
        root.phone = phone
        root.username = username
        root.password = password
        root.save()

        authenticate(request)
        login(request, root)

        return redirect('home')


    context = {

    }
    return render(request,'register/register.html' , context)

def SignIn(request):
    if not request.user.is_anonymous:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user.password == password:
            context = {
                "error": True
            }
            login(request, user)

            return redirect('home')

        if not user:
            context = {
                "error" : True
            }
            return render(request, '../templates/register/login.html',context)

        if not user.check_password(password):
            context = {
                "error" : True
            }
            return render(request,'../templates/register/login.html',context)

        login(request, user)

        return redirect('home')


    context = {

    }
    return render(request,'register/login.html' , context)

def LogOut(request , conf=False):
    if not conf:
        return render(request , 'register/logout.html')
    logout(request)
    context = {

    }
    return redirect('sign-in')