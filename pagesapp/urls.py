from django.urls import path

from .views import *

urlpatterns = [
    path('' , index , name = 'home'),
    path('catalog/' , catalog , name = 'catalog'),
    path('cart/' , cart , name = 'cart'),
    path('compare' , compare , name = 'compare'),
    path('contacts/' , contacts , name = 'contacts'),
    path('product' , product , name = 'product'),
    path('add-cart/<int:pk>/<url>' , add_cart , name = 'add_cart'),
    path('delete-cart/<int:pk>/' , delete_cart , name = 'delete_cart'),
    path('delete-all-cart/' , delete_all_cart , name = 'delete_all_cart'),
]