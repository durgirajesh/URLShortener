from django.urls import path
from . import views

urlpatterns = [
    path('url/', views.url_shortener, name='url_shortener')
]