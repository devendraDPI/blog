from django.shortcuts import get_object_or_404, render
from blog.models import Blog, Category

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
