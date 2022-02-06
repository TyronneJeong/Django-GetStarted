from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author' : 'baekgooni',
        'title': 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'Feburary 6, 2021'
    },
    {
        'author' : 'baekgooni',
        'title': 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'Feburary 6, 2021'
    },
]

def home(request):
    context = {
        # 'posts':posts
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'Fisrt Move'})