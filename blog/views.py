from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':   'CoreyMS',
        'title':    'Blog Post 1',
        'content':  'First post conent',
        'date_posted': '24.02.19'
    }

]

def home(request):
    return render(request, 'blog/home.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})
