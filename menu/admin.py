from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Post, Category


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)