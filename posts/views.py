from django.shortcuts import render
from .models import Posts

def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, id):
    posts = Posts.objects.get(id=id)
    return render(request, 'post.html', {'posts': posts})