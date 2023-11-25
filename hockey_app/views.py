from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
from datetime import datetime
import calendar
from calendar import HTMLCalendar
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # this will pop up a message if they get pass/user wrong
from django.contrib.auth.forms import UserCreationForm


def index(request):
    current_datetime = datetime.now()
    year=current_datetime.year
    month=current_datetime.strftime('%B') # Full month name, e.g., 'November'
    month_number = current_datetime.month # convert month f/ name to #
    month_number = int(month_number) # ensure that month is an int

    # create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    players_registered = Player.objects.all()
    # print("Player's registered to Adult Hockey League ", players_registered)
    return render( request, 'hockey_app/index.html', {'players_registered':players_registered, "year": year, "month": month, "month_number": month_number, "cal": cal})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username'] # Get the username 
        password = request.POST['password'] # Get the password
        user = authenticate(request, username=username, password=password) 
        # make sure it checks out and is correct info
        if user is not None:
            login(request, user) # this is using the login function that we imported thru django
            messages.success(request, ("You have been logged in!"))
            return redirect('index')
        else:
            messages.success(request, ("Error: login not successful, please try again."))
            return render( request, 'hockey_app/login.html', {}) # redirect to the login page
    else:
        return render( request, 'hockey_app/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # this will give the django form 
        if form.is_valid():
            form.save()
            # below we santitize the feild inputs -- good for cyber security and safe coding practices
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] # there typically two passwords that you type in when registering 
            # authenticate user & sign in user after creation of account
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
    else:   # this means that the form hasn't been filled out so we need to sent it
        form = UserCreationForm()
    return render(request, 'hockey_app/register_user.html', {'form':form,})

class PlayerListView(generic.ListView):
   model = Player
class PlayerDetailView(generic.DetailView):
   model = Player


def createPlayer(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player')  # Redirect to the player list page
    else:
        form = PlayerForm()  # Create an empty form for GET requests
    return render(request, 'hockey_app/player_form.html', {'form': form})


def deletePlayer(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player')
    return render(request, 'hockey_app/player_delete.html', {'player': player})


def updatePlayer(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player-detail', pk=player.id)
    else:
        form = PlayerForm(instance=player)
    context = {'form': form, 'player': player}
    return render(request, 'hockey_app/update_player.html', context)