
from django.urls import path
from .views import *

urlpatterns = [
    path('createShortUrl/', CreateShortUrlView.as_view()),
    path('listUrl/', ListAllUrlView.as_view()),    
    path('<str:shorturl>',redirectUrl),
]