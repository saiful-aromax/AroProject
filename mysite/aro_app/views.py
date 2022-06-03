from django.shortcuts import render
from django.http import HttpResponse
from . utility import layout

# Create your views here.
def home(request):
 AroVar = {"alpha":"A", "bita": "B", "gamma": 'C'}
 return layout(request, 'home.html', AroVar)
 
 # return layout(request, 'home.html', AroVar)
  # return render(request, 'layout.html')