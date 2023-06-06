from django.shortcuts import redirect, render
from blog.models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except Exception:
        return redirect('home')
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts-by-category.html', context)
