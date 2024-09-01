from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def index_blog(request):
    posts = Post.objects.all().order_by("-created_on")
    context={
        "posts": posts,
        
    }
    return render(request, "blog/index.html", context)




# Category View

def category_blog(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts
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

