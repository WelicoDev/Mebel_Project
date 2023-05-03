from django.urls import path
from .views import *

urlpatterns =[
    path('' , lists , name ='ctg_list'),
    path('detail/<int:pk>' , detail , name ='ctg_detail'),
    path('edit//<int:pk>' , edit , name ='ctg_edit'),
    path('add/' , add , name ='ctg_add'),
    path('delete/<int:pk>' , delete , name ='ctg_delete'),
]