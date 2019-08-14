from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

	ID = models.CharField(max_length = 120, primary_key=True)
	mtype = models.CharField(max_length = 120)
	primTitle = models.CharField(max_length = 120)
	originalTitle = models.CharField(max_length = 120)
	isAdult = models.BooleanField()
	startyear = models.DecimalField(max_digits =10, decimal_places=0)
	endyear = models.DecimalField(max_digits =10, decimal_places=0)
	runtime = models.DecimalField(max_digits =10, decimal_places=0	)
	genres = models.CharField(max_length = 120)
	isBooked = models.BooleanField()
	price = models.DecimalField(decimal_places = 2 , max_digits=10000)
	poster = models.CharField(max_length = 120)
	description = models.TextField(max_length = 120)

class Payment(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	ID = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
	price = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')

class BookedProduct(models.Model):
	ID = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
	username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	returnBy = models.DateField(auto_now=False)

class Client(models.Model):
	name = models.CharField(max_length = 120)
	surname =models.CharField(max_length = 120)
	IdNumber = models.CharField(max_length = 20)
	contactNumber = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 120)
	address = models.CharField(max_length = 120)
	username = models.CharField(max_length = 120)
	password = models.CharField(max_length = 120)