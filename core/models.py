from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    user = models.OneToOneField(User,related_name='address', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street=models.CharField(max_length=100,null=True,blank=True)
    long_x=models.FloatField()
    lat_y=models.FloatField()
    description=models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.user.username
    

class Order(models.Model):
    stat = (
        ('Shipped', 'Shipped'),
        ('Not Shipped', 'Not Shipped'),
    )
    shipp_type= (
        ('Express Shipping', 'Express Shipping'),
        ('Standard shipping', 'Standard shipping'),
    )
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    status_field = models.CharField(max_length=30, choices=stat)
    shipping_type=models.CharField(max_length=30, choices=shipp_type)
    total = models.FloatField(default=0)
    
    def __str__(self):
        return self.customer.username



class Tools(models.Model):
    item_name = models.CharField(max_length=200)
    address = models.ForeignKey(Address,related_name='Tools', on_delete=models.CASCADE)
    item_description= models.CharField(max_length=500,null=True,blank=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    item_price = models.FloatField()
    shipping_cost=models.FloatField()
    image_tools=models.ImageField()
    order = models.ForeignKey(Order,related_name='Tools', on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.item_name
    
