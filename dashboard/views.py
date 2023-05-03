from django.shortcuts import render

# Create your views here.

def index(requests):
    context ={

    }
    return render(requests,'dashboard/base.html',context)
