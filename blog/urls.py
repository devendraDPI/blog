from django.urls import path
from blog import views


urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts-by-category'),
]
