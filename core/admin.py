from django.contrib import admin
from .models import *

@admin.register(Address)
class PostAdmin(admin.ModelAdmin):
    list_display = ['city','neighborhood', 'street','long_x','lat_y']
    list_filter = ['city','neighborhood', 'street']
    search_fields = ['city','neighborhood', 'street']
    ordering = ['city','neighborhood', 'street']


@admin.register(Tools)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_description', 'quantity', 'item_price','shipping_cost']


@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','order_date', 'status_field', 'shipping_type','total']
    

