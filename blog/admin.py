from django.contrib import admin
from blog.models import Category, Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status',
                    'is_featured', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'category__category_name',
                    'author', 'status')
    list_editable = ('status', 'is_featured',)
    list_per_page = 10


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
