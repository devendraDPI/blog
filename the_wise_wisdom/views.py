from django.shortcuts import render
from blog.models import Category, Blog


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status='published').order_by('updated_at')
    posts = Blog.objects.filter(
        is_featured=False, status='published')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)
