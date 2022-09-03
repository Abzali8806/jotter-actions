from re import search
from random import randint
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    post_ids = []

    count = 0
    while count < 3:
        num = randint(1, len(posts))
        while num in post_ids:
            num = randint(1, len(posts))
        post_ids.append(num)
        count += 1
    
    context = {
        'posts': posts,
        'pids': post_ids
    }
    return render(request, "main/index.html", context)


def blog_view(request):
    posts = Post.objects.all()
    search = request.GET['sc']
    context = {
        'posts': posts,
        'search': search
    }
    return render(request, "main/blog.html", context)


def create_post_view(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect(home_view)
    
    context = {
        "form": form
    }
    return render(request, "main/create_post.html", context)


def post_view(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
        'search': search
    }
    return render(request, "main/post.html", context)
