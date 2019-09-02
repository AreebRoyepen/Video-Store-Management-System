from django.contrib import admin
from .models import Product, Payment, BookedProduct, Client

# Register your models here.

admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(BookedProduct)
admin.site.register(Client)
