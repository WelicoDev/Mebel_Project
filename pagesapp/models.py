from django.db import models
from django.utils.text import slugify
from accounts.models import User

# Create your models here.
def price_choise():
    return [
        ("USD" , "USD"),
        ("RUB", "RUB"),
        ("EUR" , "EUR"),
        ("UZS", "UZS"),
    ]

class Category(models.Model):
    img = models.ImageField(upload_to="sayt")
    content = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256 ,null=True , blank=True )

    def save(self , *args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.content)

        return super(Category , self ).save(*args,**kwargs)
    def __str__(self):
        return self.content

class Product(models.Model):
    ctg = models.ForeignKey(Category , on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    price_type = models.CharField( max_length=16 , choices=price_choise())
    len = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    is_bed = models.BooleanField(default=False)
    bed_len = models.IntegerField(null=True, blank=True)
    bed_width = models.IntegerField(null=True, blank=True)
    bed_height = models.IntegerField(null=True, blank=True)

    update_dt = models.DateTimeField(auto_now_add=False , auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True , auto_now=False)

    def __str__(self):
        return self.name

class ProImg(models.Model):
    prod = models.ForeignKey(Product, on_delete = models.CASCADE)
    img = models.ImageField()

    update_dt = models.DateTimeField(auto_now_add=False , auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True , auto_now=False)

    def __str__(self):
        return self.prod.name

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete =models.CASCADE)
    dona = models.IntegerField(default=1)
    umumiy = models.IntegerField(default=0)
    update_dt = models.DateTimeField(auto_now_add=False , auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True , auto_now=False)

    def save(self,*args, **kwargs):
        self.umumiy =self.dona * self.product.price

        return super(Cart, self).save(*args , **kwargs)

    def __str__(self):
        return self.product
