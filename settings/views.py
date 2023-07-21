from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    contacts = Contacts.objects.all()
    news = News.objects.all()
    context = {
        'setting': setting,
        'contacts':contacts,
        'news':news,
    }
    return render(request,'index.html',context)

def news_detail(request,id):
    new = News.objects.get(id=id)
    context={
        'new':new,
    }
    return render(request,'news_detail.html',context)