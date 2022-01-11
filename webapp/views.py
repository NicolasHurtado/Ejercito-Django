from django.shortcuts import render
from soldados.models import Arma

# Create your views here.
def home(request):
    return render(request,'home.html')


