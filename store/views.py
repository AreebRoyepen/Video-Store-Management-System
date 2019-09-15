from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.template import RequestContext
from django.shortcuts import render_to_response



from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

from .models import Product
from .models import BookedProduct



def home(request):


    latest_slide_1 = Product.objects.filter(genres__icontains='Action', isBooked=False)[0:4]
    latest_slide_2 = Product.objects.filter(genres__icontains='Comedy', isBooked=False)[0:4]
    latest_slide_3 = Product.objects.filter(genres__icontains='Family', isBooked=False)[0:4]
    latest_slide_4 = Product.objects.filter(genres__icontains='Horror', isBooked=False)[0:4]

    action_slide_1 = Product.objects.filter(genres__icontains='Action', isBooked=False)[0:4]
    action_slide_2 = Product.objects.filter(genres__icontains='Action', isBooked=False)[5:9]
    action_slide_3 = Product.objects.filter(genres__icontains='Action', isBooked=False)[8:12]
    action_slide_4 = Product.objects.filter(genres__icontains='Action', isBooked=False)[12:16]

    comedy_slide_1 = Product.objects.filter(genres__icontains='Comedy', isBooked=False)[0:4]
    comedy_slide_2 = Product.objects.filter(genres__icontains='Comedy', isBooked=False)[4:8]
    comedy_slide_3 = Product.objects.filter(genres__icontains='Comedy', isBooked=False)[8:12]
    comedy_slide_4 = Product.objects.filter(genres__icontains='Comedy', isBooked=False)[12:16]


    family_slide_1 = Product.objects.filter(genres__icontains='Family', isBooked=False)[0:4]
    family_slide_2 = Product.objects.filter(genres__icontains='Family', isBooked=False)[4:8]
    family_slide_3 = Product.objects.filter(genres__icontains='Family', isBooked=False)[8:12]
    family_slide_4 = Product.objects.filter(genres__icontains='Family', isBooked=False)[12:16]

    horror_slide_1 = Product.objects.filter(genres__icontains='Horror', isBooked=False)[0:4]


    args = { 
        'latest_slide_1':latest_slide_1 ,'latest_slide_2':latest_slide_2,'latest_slide_3':latest_slide_3,'latest_slide_4':latest_slide_4,
        'action_slide_1':action_slide_1 ,'action_slide_2':action_slide_2,'action_slide_3':action_slide_3,'action_slide_4':action_slide_4,
        'comedy_slide_1':comedy_slide_1 ,'comedy_slide_2':comedy_slide_2,'comedy_slide_3':comedy_slide_3,'comedy_slide_4':comedy_slide_4,
        'family_slide_1':family_slide_1 ,'family_slide_2':family_slide_2,'family_slide_3':family_slide_3,'family_slide_4':family_slide_4,
        'horror_slide_1':horror_slide_1
        }






    return render(request, "store/home.html", args)

def about(request):
	return render(request,"store/about.html")  

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  dj_login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print("invalid login details " + username + " " + password)
              return render(request, 'login.html', {})
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'store/login.html', {})

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
                return HttpResponseRedirect("/")

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

    #return render(request, 'store/home.html')

def user_rentals(request):

    movies = BookedProduct.objects.filter(ID=User.id)
    args = {
        'rented_movies':movies
    }
    return render(request,"store/rentalsPage.html", args) 


def book(request):
    print("check")
    if request.method == "POST":
        movie_id = request.POST['movie_id']
        movie = Product.objects.filter(ID= movie_id).update(isBooked=True)
        print("\n\n\n\n\n\n\n" + movie_id + "\n\n\n\n\n\n")
        rented_movie = BookedProduct()
        rented_movie.ID_id = movie
        rented_movie.username_id = User.username
        rented_movie.save(force_insert=True)
        movie.save()
    return HttpResponseRedirect("/")
