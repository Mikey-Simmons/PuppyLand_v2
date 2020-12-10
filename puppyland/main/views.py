from django.shortcuts import render
from .models import Dog, User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')