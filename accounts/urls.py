from django.urls import path
from .views import *



urlpatterns = [
    path('' , SignUp , name = 'sign-up'),
    path('login/' , SignIn , name = 'sign-in'),
    path('logout/' , LogOut , name = 'log-out'),
    path('logout/<conf>/' , LogOut , name = 'log-out-conf')
]