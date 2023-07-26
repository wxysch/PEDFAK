from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('news_detail/<int:id>/',news_detail,name='news_details'),
    path('safety/',safety,name='safety'),
    path('information/',information,name='information'),
    path('department/',department,name='department'),
    path('biography/',biography,name='biography'),
    path('appeal/',appeal,name='appeal'),
    path('announcement/',announcement,name='announcement'),
    path('albums/',albums,name='albums'),
    path('search/',news_search,name="search"),
    path('videos/',videos,name='videos'),
]