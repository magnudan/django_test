from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
