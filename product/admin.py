from django.contrib import admin
from .models import Product, Variation, Category, SubCategory, MoreImages, MoreImagesVariation
from . import models
# Register your models here.


class CategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]

    inlines = [
        CategoryInline
    ]


class MoreImagesVariationInline(admin.TabularInline):
    model = MoreImagesVariation
    extra = 1


class MorImagesInline(admin.TabularInline):
    model = MoreImages
    extra = 0


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1
    inlines = [
        MoreImagesVariationInline
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", "category", "is_available",
                    'short_description', 'price', 'promotion_price']
    inlines = [
        MorImagesInline, VariationInline
    ]


class VariationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_available', 'stock', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

#admin.site.register(CategoryFromCategory, CategoryInline)
