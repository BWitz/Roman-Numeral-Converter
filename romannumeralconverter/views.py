from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(response):
    return render(response, "romannumeralconverter/home.html", {})

def index(response, arabic_num):
    return render(response,"romannumeralconverter/index.html", {"number":arabic_num})