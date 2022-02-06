from django.urls import path
from . import views

urlpatterns = [
    # /blog/home
    path('', views.home, name='blog-home'),
    
    # /blog/about
    path('about/', views.about, name='blog-about'),
]
