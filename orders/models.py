from django.db import models
from stores.models import Product,User


# Create your models here.
class Basket(models.Model):

    create_time=models.DateField(auto_now_add=True)
    payment=models.BooleanField(default=False)
    update_time=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    class Meta :
        ordering=['create_time',] 


class BasketItem(models.Model):
    create_time=models.DateField(auto_now_add=True)
    amount=models.PositiveSmallIntegerField()
    price=models.PositiveSmallIntegerField()
    update_time=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE)
    product_item=models.ForeignKey(Product,on_delete=models.CASCADE)
    class Meta :
        ordering=['price',] 



class Order(models.Model):
 
    create_time=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering=[ 'create_time',]
    

    
    