from django.shortcuts import render
from blog.models import Announcement, Blog


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status='published').order_by('updated_at')
    posts = Blog.objects.filter(
        is_featured=False, status='published')
    announcements = Announcement.objects.filter(
        is_announce=True).order_by('-updated_at')[:len(posts)]
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'announcements': announcements,
    }
    return render(request, 'home.html', context)
