from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   # Render index.html
   return render( request, 'hockey_app/index.html')