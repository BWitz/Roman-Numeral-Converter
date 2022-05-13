from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from romannumeralconverter.models import Numeral
# Create your views here.

def home(response):
    return render(response, "romannumeralconverter/home.html", {})

def index(response, arabic_num):
    roman_num = Numeral.integerToRoman(arabic_num)
    return render(response,"romannumeralconverter/index.html", {"arabic_number":arabic_num, "roman_number": roman_num})