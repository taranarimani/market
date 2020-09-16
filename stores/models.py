from django.db import models
from accounts.models import User

# Create your models here.


class Store(models.Model):
    name=models.CharField(max_length=100)
    create_time=models.DateField(auto_now_add=True)
    update_time=models.DateField(auto_now=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='stores')
    class Meta:
        ordering=['-name',]
        verbose_name_plural = "store name"

    


class Product(models.Model):
    name=models.CharField(max_length=100)
    create_time=models.DateField(auto_now_add=True)
    price=models.SmallIntegerField()
    is_enable=models.BooleanField(default=True)
    update_time=models.DateField(auto_now=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name='products')
    class Meta:
        ordering=['-name',]
        verbose_name_plural="product name"



