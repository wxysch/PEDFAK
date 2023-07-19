from django.shortcuts import render
from .models import *
# Create your views here.
def index(a):
    setting = Settings.objects.latest('id')
    contacts = Contacts.objects.all()
    context = {
        'setting': setting,
        'contacts':contacts
    }
    return render(a,'index.html',context)