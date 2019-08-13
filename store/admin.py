from django.contrib import admin
from .models import Media, Payment, Booked

# Register your models here.

admin.site.register(Media)
admin.site.register(Payment)
admin.site.register(Booked)