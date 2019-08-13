from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Media(models.Model):

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
	ID = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='+')
	price = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='+')

class Booked(models.Model):
	ID = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='+')
	username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	#returnBy = getDateForWhenToReturnTo()