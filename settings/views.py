from django.shortcuts import render


# Create your views here.
def index(a):
    return render(a,'index.html')