from django.contrib import admin
from blog.models import Category, Blog, Announcement, BlogComment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status',
                    'is_featured', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'category__category_name',
                    'author', 'status')
    list_editable = ('status', 'is_featured',)
    list_per_page = 10


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'created_at', 'updated_at')
    list_per_page = 10


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_announce', 'created_at', 'updated_at')
    search_fields = ('title', 'description',)
    list_editable = ('is_announce',)
    list_per_page = 10


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
