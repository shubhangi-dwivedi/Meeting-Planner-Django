from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse("Tis page was served at " + str(datetime.now()))