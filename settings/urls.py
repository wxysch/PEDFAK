from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('news_detail/<int:id>/',news_detail,name='news_details')
]