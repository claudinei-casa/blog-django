from django.contrib import admin
from .models import Post


# admin.site.register(Post)

# to review
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created_on", "last_modified")
    list_filter = ("created_on", "author", "title")
    search_fields = ("title", "body", "slug")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["last_modified", "created_on"]
