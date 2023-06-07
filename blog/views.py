from django.shortcuts import get_object_or_404, render
from blog.models import Blog, BlogComment, Category
from django.db.models import Q
from django.http import HttpResponseRedirect

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
    if request.method == 'POST':
        comment = BlogComment()
        comment.user = request.user
        comment.blog = article
        comment.comment = request.POST.get('comment')
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = BlogComment.objects.filter(blog=article).order_by('-created_at')
    comments_count = comments.count()
    context = {
        'article': article,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'blog.html', context)


def search(request):
    query = request.GET.get('query')
    blogs = Blog.objects.filter(Q(title__icontains=query) | Q(
        short_description__icontains=query) | Q(blog_body__icontains=query), status='published')
    context = {'query': query, 'blogs': blogs}
    return render(request, 'search.html', context)
