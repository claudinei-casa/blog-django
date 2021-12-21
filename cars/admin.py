from django.contrib import admin

from .models import Cars, Opt, Brands


# admin.site.register(Opt)
@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ("brand",)


@admin.register(Opt)
class OptAdmin(admin.ModelAdmin):
    list_display = ("opt",)


@admin.register(Cars)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "model", "year", "color",
                    "price", "mileage", "description", "usr", "get_brands_admin",)
    list_filter = ("model", "color", "title",)
    search_fields = ("year", "title", "model",)
    ordering = ["title", "year"]
