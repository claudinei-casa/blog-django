from django.contrib import admin

from .models import Cars


@admin.register(Cars)
class PostAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "slug", "year", "color",
                    "price", "mileage", "description")
    list_filter = ("model", "color", "make", "slug")
    search_fields = ("make", "model", "slug")
    prepopulated_fields = {"slug": ("make", "model",)}
    ordering = ["make", "year"]
