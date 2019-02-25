from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':   'Magnus',
        'title':    'Blog Post 1',
        'content':  'First post conent',
        'date_posted': '24.02.19'
    },
    {
        'author':   'Live',
        'title':    'Blog Post 2',
        'content':  'Second post conent',
        'date_posted': '25.02.19'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def post_list(request):
    return render(request, 'blog/post_list.html', {})
