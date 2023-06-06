from django.shortcuts import redirect, render
from blog.models import Announcement, Blog
from the_wise_wisdom.forms import SignupForm


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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)
