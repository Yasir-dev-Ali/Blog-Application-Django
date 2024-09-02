from django.shortcuts import render , get_object_or_404
from .models import Category, Post, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)




# Category View

def blog_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category).order_by("-created_on")
    context = {
        "category": category.name,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)




# Blog Detail View

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)

