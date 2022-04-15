from django.contrib import admin
from .models import Product, Variation, Category
from . import models
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", "category", "is_available",
                    'short_description', 'price', 'promotion_price']
    inlines = [
        VariationInline
    ]


class VariationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_available', 'stock', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
