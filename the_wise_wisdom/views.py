from django.shortcuts import redirect, render
from blog.models import Announcement, Blog
from the_wise_wisdom.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status='published').order_by('updated_at')
    posts = Blog.objects.filter(
        is_featured=False, status='published').order_by('-created_at')
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
            return redirect('signin')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'signin.html', context)


def signout(request):
    auth.logout(request)
    return redirect('home')
