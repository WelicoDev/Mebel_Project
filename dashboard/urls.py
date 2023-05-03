from django.urls import path , include
from .views import *

urlpatterns = [
    path('' , index , name ='dashboard_home'),

    path('ctg/', include('dashboard.ctg.urls'))
]