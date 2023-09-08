from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Post, Comment, PostCategory, Category, Author

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Category)
admin.site.register(Author)

