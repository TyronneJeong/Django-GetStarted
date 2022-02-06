from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # /blog/home
    path('', PostListView.as_view(), name='blog-home'),
    
    # /blog/detail
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # /blog/new
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # /blog/update
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    # /blog/delete
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # /blog/about
    path('about/', views.about, name='blog-about'),
]
