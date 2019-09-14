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



def home(request):

    latest_1 = Product.objects.get(originalTitle = 'Avengers: Endgame')
    latest_2 = Product.objects.get(originalTitle = 'Kill Bill: Vol. 1')
    latest_3 = Product.objects.get(originalTitle = "Howl's Moving Castle")
    latest_4 = Product.objects.get(originalTitle = 'My Neighbor Totoro')
    latest_5 = Product.objects.get(originalTitle = 'Guardians of the Galaxy')
    latest_6 = Product.objects.get(originalTitle = 'Avengers: Infinity War')
    latest_7 = Product.objects.get(originalTitle = 'Spirited Away')
    latest_8 = Product.objects.get(originalTitle = 'The Matrix')    
    latest_9 = Product.objects.get(originalTitle = 'Snatch')
    latest_10 = Product.objects.get(originalTitle = 'Yojimbo')
    latest_11 = Product.objects.get(originalTitle = 'Spider-Man: Into the Spider-Verse')
    latest_12 = Product.objects.get(originalTitle = 'Logan')
    latest_13 = Product.objects.get(originalTitle = 'Alien')
    latest_14 = Product.objects.get(originalTitle = 'Terminator 2: Judgment Day')
    latest_15 = Product.objects.get(originalTitle = 'The Gold Rush')
    latest_16 = Product.objects.get(originalTitle = 'Logan')

    latest_slide_1 = [latest_1, latest_2, latest_3, latest_4]
    latest_slide_2 = [latest_5, latest_6, latest_7, latest_8]
    latest_slide_3 = [latest_9, latest_10, latest_11, latest_12]
    latest_slide_4 = [latest_13, latest_14, latest_15, latest_16]


    action_1 = Product.objects.get(originalTitle = 'Raiders of the Lost Ark')
    action_2 = Product.objects.get(originalTitle = 'Avengers: Infinity War')
    action_3 = Product.objects.get(originalTitle = 'Dangal')
    action_4 = Product.objects.get(originalTitle = 'The Matrix')
    action_5 = Product.objects.get(originalTitle = 'Guardians of the Galaxy')
    action_6 = Product.objects.get(originalTitle = 'Rush')
    action_7 = Product.objects.get(originalTitle = 'Mad Max: Fury Road')
    action_8 = Product.objects.get(originalTitle = 'Batman Begins')    
    action_9 = Product.objects.get(originalTitle = 'The Dark Knight Rises')
    action_10 = Product.objects.get(originalTitle = 'Kill Bill: Vol. 1')
    action_11 = Product.objects.get(originalTitle = 'Memories of Murder')
    action_12 = Product.objects.get(originalTitle = 'Gladiator')
    action_13 = Product.objects.get(originalTitle = 'Logan')
    action_14 = Product.objects.get(originalTitle = 'Terminator 2: Judgment Day')
    action_15 = Product.objects.get(originalTitle = 'Blade Runner')
    action_16 = Product.objects.get(originalTitle = 'Avengers: Endgame')

    action_slide_1 = [action_1, action_2, action_3, action_4]
    action_slide_2 = [action_5, action_6, action_7, action_8]
    action_slide_3 = [action_9, action_10, action_11, action_12]
    action_slide_4 = [action_13, action_14, action_15, action_16]



    comedy_1 = Product.objects.get(originalTitle = 'Once Upon a Time in... Hollywood')
    comedy_2 = Product.objects.get(originalTitle = 'Green Book')
    comedy_3 = Product.objects.get(originalTitle = 'PK')
    comedy_4 = Product.objects.get(originalTitle = 'The Grand Budapest Hotel')
    comedy_5 = Product.objects.get(originalTitle = 'Guardians of the Galaxy')
    comedy_6 = Product.objects.get(originalTitle = 'Toy Story 4')
    comedy_7 = Product.objects.get(originalTitle = 'Up')
    comedy_8 = Product.objects.get(originalTitle = 'Toy Story 3')    
    comedy_9 = Product.objects.get(originalTitle = 'Snatch')
    comedy_10 = Product.objects.get(originalTitle = 'Monsters, Inc.')
    comedy_11 = Product.objects.get(originalTitle = 'The Big Lebowski')
    comedy_12 = Product.objects.get(originalTitle = 'The Truman Show')
    comedy_13 = Product.objects.get(originalTitle = 'Monty Python and the Holy Grail')
    comedy_14 = Product.objects.get(originalTitle = 'Dead Poets Society')
    comedy_15 = Product.objects.get(originalTitle = 'Back to the Future')
    comedy_16 = Product.objects.get(originalTitle = 'Yojimbo')

    comedy_slide_1 = [comedy_1, comedy_2, comedy_3, comedy_4]
    comedy_slide_2 = [comedy_5, comedy_6, comedy_7, comedy_8]
    comedy_slide_3 = [comedy_9, comedy_10, comedy_11, comedy_12]
    comedy_slide_4 = [comedy_13, comedy_14, comedy_15, comedy_16]


    family_1 = Product.objects.get(originalTitle = 'Up')
    family_2 = Product.objects.get(originalTitle = "Hachi: A Dog's Tale")
    family_3 = Product.objects.get(originalTitle = 'How to Train Your Dragon')
    family_4 = Product.objects.get(originalTitle = 'Toy Story 3')
    family_5 = Product.objects.get(originalTitle = 'Spirited Away')
    family_6 = Product.objects.get(originalTitle = 'Monsters, Inc.')
    family_7 = Product.objects.get(originalTitle = "Howl's Moving Castle")
    family_8 = Product.objects.get(originalTitle = 'My Neighbor Totoro')    
    family_9 = Product.objects.get(originalTitle = 'The Kid')
    family_10 = Product.objects.get(originalTitle = 'Coco')
    family_11 = Product.objects.get(originalTitle = 'Inside Out')
    family_12 = Product.objects.get(originalTitle = 'Chak de! India')
    family_13 = Product.objects.get(originalTitle = 'Children of Heaven')
    family_14 = Product.objects.get(originalTitle = 'The Princess Bride')
    family_15 = Product.objects.get(originalTitle = "It's a Wonderful Life")
    family_16 = Product.objects.get(originalTitle = 'The Gold Rush')

    family_slide_1 = [family_1, family_2, family_3, family_4]
    family_slide_2 = [family_5, family_6, family_7, family_8]
    family_slide_3 = [family_9, family_10, family_11, family_12]
    family_slide_4 = [family_13, family_14, family_15, family_16]

    
    horror_1 = Product.objects.get(originalTitle = 'The Shining')
    horror_2 = Product.objects.get(originalTitle = 'Alien')
    horror_3 = Product.objects.get(originalTitle = 'Psycho')
    horror_4 = Product.objects.get(originalTitle = 'The Thing')
    horror_5 = Product.objects.get(originalTitle = 'The Third Man')
    horror_6 = Product.objects.get(originalTitle = 'Avengers: Infinity War')
    horror_7 = Product.objects.get(originalTitle = 'Spider-Man: Into the Spider-Verse')
    horror_8 = Product.objects.get(originalTitle = 'Logan')    
    horror_9 = Product.objects.get(originalTitle = 'Avengers: Endgame')
    horror_10 = Product.objects.get(originalTitle = 'Avengers: Infinity War')
    horror_11 = Product.objects.get(originalTitle = 'Spider-Man: Into the Spider-Verse')
    horror_12 = Product.objects.get(originalTitle = 'Logan')
    horror_13 = Product.objects.get(originalTitle = 'Avengers: Endgame')
    horror_14 = Product.objects.get(originalTitle = 'Avengers: Infinity War')
    horror_15 = Product.objects.get(originalTitle = 'Spider-Man: Into the Spider-Verse')
    horror_16 = Product.objects.get(originalTitle = 'Logan')

    horror_slide_1 = [horror_1, horror_2, horror_3, horror_4]
    horror_slide_2 = [horror_5, horror_6, horror_7, horror_8]
    horror_slide_3 = [horror_9, horror_10, horror_11, horror_12]
    horror_slide_4 = [horror_13, horror_14, horror_15, horror_16]    
   
    args = { 
        'latest_slide_1':latest_slide_1 ,'latest_slide_2':latest_slide_2,'latest_slide_3':latest_slide_3,'latest_slide_4':latest_slide_4,
        'action_slide_1':action_slide_1 ,'action_slide_2':action_slide_2,'action_slide_3':action_slide_3,'action_slide_4':action_slide_4,
        'comedy_slide_1':comedy_slide_1 ,'comedy_slide_2':comedy_slide_2,'comedy_slide_3':comedy_slide_3,'comedy_slide_4':comedy_slide_4,
        'family_slide_1':family_slide_1 ,'family_slide_2':family_slide_2,'family_slide_3':family_slide_3,'family_slide_4':family_slide_4,
        'horror_slide_1':horror_slide_1 ,'horror_slide_2':horror_slide_2,'horror_slide_3':horror_slide_3,'horror_slide_4':horror_slide_4 
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


def book(request):
	return render(request,"store/book.html")