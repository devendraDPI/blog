from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
BLOG_STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=1024)
    blog_body = RichTextUploadingField(max_length=16384)
    status = models.CharField(max_length=32, choices=BLOG_STATUS, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog comments'

    def __str__(self):
        return self.comment


class Announcement(models.Model):
    title = models.CharField(max_length=64)
    description = RichTextUploadingField(max_length=512)
    announce_image = models.ImageField(upload_to='uploads/announcements/%Y/%m/%d')
    is_announce = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return self.title
