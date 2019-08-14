from django.contrib import admin
from .models import Product, Payment, BookedProduct

# Register your models here.

admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(BookedProduct)