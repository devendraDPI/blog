from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add-category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit-category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete-category'),
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_post, name='add-post'),
    path('posts/edit/<int:pk>/', views.edit_post, name='edit-post'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete-post'),
]
