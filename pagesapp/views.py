from django.shortcuts import render ,redirect
from .models import *

# Create your views here.

def index(request):
    mebels=Product.objects.all().order_by("-pk")
    ctg = Category.objects.all()
    context = {
         "mebels": mebels,
         "ctg" : ctg,
    }
    return render(request, 'site/index.html' , context)

def catalog(request):
    mebels=Product.objects.all().order_by("-pk")
    ctg = Category.objects.all()
    context = {
         "mebels": mebels,
         "ctg" : ctg,
    }
    return render(request, 'site/catalog.html' , context)

def add_cart(request, pk ,url="home"):
    if request.user.is_anonymous:
        return redirect("sign-in")

    root = Product.objects.get(pk=pk)
    cart = Cart.objects.filter(product=root,user=request.user).first()

    if cart:
        cart.dona += 1
        cart.save()
        return redirect(url)

    savat=Cart()
    savat.product = root
    savat.user = request.user
    savat.save()


    return redirect(url)

def delete_cart(request, pk):
    if request.user.is_anonymous:
        return redirect("sign-in")

    Cart.objects.get(pk=pk).delete()
    return redirect("cart")

def delete_all_cart(request):
    if request.user.is_anonymous:
        return redirect("sign-in")

    Cart.objects.filter(user=request.user).delete()

    return redirect("cart")


def cart(request):
    if request.user.is_anonymous:
        return redirect("sign-in")

    cart = Cart.objects.filter(user=request.user)
    context = {
        "cart" : cart,
        "len" :len(cart)
    }
    return render(request, 'site/cart.html' , context)

def compare(request):
    context = {

    }
    return render(request, 'site/compare.html' , context)

def contacts(request):
    context = {

    }
    return render(request, 'site/contacts.html' , context)

def product(request):
    context = {

    }
    return render(request, 'site/product.html' , context)