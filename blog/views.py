from django.shortcuts import get_object_or_404, render
from blog.models import Blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except Exception:
        return render(request, '404.html')
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts-by-category.html', context)


def blogs(request, slug):
    article = get_object_or_404(Blog, slug=slug, status='published')
    context = {'article': article}
    return render(request, 'blog.html', context)


def search(request):
    query = request.GET.get('query')
    blogs = Blog.objects.filter(Q(title__icontains=query) | Q(
        short_description__icontains=query) | Q(blog_body__icontains=query), status='published')
    context = {'query': query, 'blogs': blogs}
    return render(request, 'search.html', context)
