from blog.models import Category
from decouple import config


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_social_links(request):
    social_links = {
        'github': config('GITHUB'),
        'twitter': config('TWITTER'),
        'facebook': config('FACEBOOK'),
        'youtube': config('YOUTUBE'),
    }
    return {'social_links': social_links}
