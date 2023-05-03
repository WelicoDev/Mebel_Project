from django.contrib import admin
from .models import *
# Register your models here.


class ImgInline(admin.StackedInline):
    model = ProImg
    extra = 2

class ProdAdmin(admin.ModelAdmin):
    model = Product
    inlines =[ImgInline]


admin.site.register(Category)
admin.site.register(Product , ProdAdmin)
