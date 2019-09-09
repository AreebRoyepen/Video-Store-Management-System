from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm



def home(request):
	return render(request, "store/home.html")

def about(request):
	return render(request,"store/about.html")  

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            dj_login(request, user)
            # Success, now let's login the user.
            return render(request, 'store/home.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'store/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'store/login.html')

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'store/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user_account = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                )
                user_account.save()
               
                # Login the user
                dj_login(request, user_account)
               
                # redirect to accounts page:
                return HttpResponseRedirect("")

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def book(request):
	return render(request,"store/book.html")