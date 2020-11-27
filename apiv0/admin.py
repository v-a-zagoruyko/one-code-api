from django.contrib import admin
from django.utils.html import format_html
from meta.models import ProductTypes, ProductFibers
from apiv0.models import *


class ProductTypesInline(admin.TabularInline):
    model = ProductTypes
    extra = 1

class ProductFibersInline(admin.TabularInline):
    model = ProductFibers
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_module_permission(self, request):
        return False

@admin.register(ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_module_permission(self, request):
        return False

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductFibersInline,)
    inlines = (ProductTypesInline, ProductFibersInline,)

    list_display = ('category', 'collection', 'title', 'stock', 'is_visible', 'is_available',)
    search_fields = ('title',)

    def stock(self, obj):
        if obj.product_types:
            sizes = ''
            quantity = ''

            for item in obj.product_types.all():
                sizes += '<th>{}</th>'.format(item.size)
                quantity += '<td>{}</td>'.format(item.quantity)
            return format_html('<table><tr>{}</tr><tr>{}</tr></table>'.format(sizes, quantity))

        return '-'
