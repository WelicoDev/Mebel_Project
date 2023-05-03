from django.shortcuts import render

from pagesapp.models import *

def lists(requests):
    ctgs = Category.objects.all()
    ctx = {
        "ctgs" :ctgs
    }
    return render(requests, 'dashboard/ctg/list.html' , ctx)

def detail(requests , pk):
    ctg = Category.objects.get(pk=pk)
    ctx = {
       "ctg":ctg,
    }
    return render(requests, 'dashboard/ctg/detail.html' , ctx)

def add(requests):
    ctx = {

    }
    return render(requests, 'dashboard/ctg/form.html' , ctx)

def edit(requests , pk):
    ctx = {

    }
    return render(requests, 'dashboard/ctg/form.html' , ctx)

def delete(requests , pk):
    ctx = {

    }
    pass