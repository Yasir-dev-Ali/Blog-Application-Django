from django.urls import path
from . import   views



urlpatterns = [
  path('', views.index_blog, name="blog_index"),
    path('category/<str:category>/', views.category_blog, name="blog_category"),
    path('post/<int:pk>/', views.blog_detail, name="blog_detail"),
    
    
]