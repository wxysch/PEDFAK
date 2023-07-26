from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    contacts = Contacts.objects.all()
    news = News.objects.all()
    sliders = Slider.objects.all()
    context = {
        'setting': setting,
        'contacts':contacts,
        'news':news,
        'sliders':sliders,
    }
    return render(request,'index.html',context)

def news_detail(request,id):
    new = News.objects.get(id=id)
    context={
        'new':new,
    }
    return render(request,'news_detail.html',context)

def safety(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
    }
    return render(request,'safety.html',context)

def information(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
    }
    return render(request,'information.html',context)

def department(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
    }
    return render(request,'department.html',context)

def biography(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
    }
    return render(request,'biography.html',context)

def appeal(request):
    contacts = Contacts.objects.all()
    appeals = Appeal.objects.all()
    if request.method == 'POST':
        fio = request.POST.get('fio')
        email = request.POST.get('email')
        description = request.POST.get('description')
        Appeal.objects.create(description=description,email=email,fio=fio)
        return redirect('index')
    context = {
        'contacts':contacts,
        'appeals':appeals,
    }
    return render(request,'appeal.html',context)

def announcement(request):
    announcements = Announcement.objects.all()
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
        'announcements':announcements,
    }
    return render(request,'announcement.html',context)

def albums(request):
    albums = Albums.objects.all()
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
        'albums':albums,
    }
    return render(request,'albums.html',context)

def videos(request):
    videos = Video.objects.all()
    contacts = Contacts.objects.all()
    context = {
        'contacts':contacts,
        'videos':videos,
    }
    return render(request,'videos.html',context)

def news_search(request):
    setting = Settings.objects.latest('id')
    contacts = Contacts.objects.all()
    all_news = News.objects.all()
    query_object = request.GET.get('key')
    if query_object:
        news = all_news.filter(Q(title__icontains=query_object) | Q(description__icontains=query_object))
    else:
        news = all_news
        
    context = {
        'setting': setting,
        'contacts': contacts,
        'all_news': news,
    }
    return render(request, 'search.html', context)
