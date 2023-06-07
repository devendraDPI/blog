from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Blog, Category
from django.contrib.auth.decorators import login_required
from dashboard.froms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='signin')
def dashboard(request):
    blogs_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        'blogs_count': blogs_count,
        'category_count': category_count,
    }
    return render(request, 'dashboard/dashboard.html', context)


def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {'form': form}
    return render(request, 'dashboard/add-categories.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit-categories.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all().order_by('updated_at')
    context = {'posts': posts}
    return render(request, 'dashboard/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = f'{slugify(title)}-{str(post.id)}'
            post.save()
            return redirect('posts')
    form = BlogPostForm()
    context = {'form': form}
    return render(request, 'dashboard/add-post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = f'{slugify(title)}-{str(post.id)}'
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'dashboard/edit-post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')
