from django.contrib import admin

from .models import Cars


@admin.register(Cars)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "brand", "model", "year", "color",
                    "price", "mileage", "description", "usr",)
    list_filter = ("model", "color", "brand", "title",)
    search_fields = ("brand", "year", "title", "model",)
    ordering = ["title", "brand", "year"]
