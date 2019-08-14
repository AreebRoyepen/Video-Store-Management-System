from django.shortcuts import render


def home(request):
	return render(request, "store/home.html")

def about(request):
	return render(request,"store/about.html")  

def login(request):
	return render(request,"store/login.html")