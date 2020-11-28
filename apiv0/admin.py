from django.contrib import admin
from django.utils.html import format_html
from meta.models import ProductTypes, ProductFibers
from apiv0.models import *
from apiv0.widgets import *


class ProductTypesInline(admin.TabularInline):
    model = ProductTypes
    extra = 1


class ProductFibersInline(admin.TabularInline):
    model = ProductFibers
    extra = 1


class ProductPhotosInline(admin.TabularInline):
    model = ProductPhotos
    formfield_overrides = { models.FileField: {'widget': InlineImageWidget} }
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_module_permission(self, request):
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductTypesInline, ProductFibersInline, ProductPhotosInline,)

    list_display = ('img', 'category', 'title', 'stock', 'is_visible', 'is_available',)
    list_display_links = ('img', 'category', 'title',)
    search_fields = ('title',)

    def img(self, obj):
        if obj.product_photos.first():
            url = obj.product_photos.first().image.url
            return format_html('<img style="height: 200px; width: 200px; object-fit: cover" src="{}" />'.format(url))
        return '-'

    def stock(self, obj):
        if obj.product_types:
            sizes = ''
            quantity = ''

            for item in obj.product_types.all():
                sizes += '<th>{}</th>'.format(item.size)
                quantity += '<td>{}</td>'.format(item.quantity)
            return format_html('<table><tr>{}</tr><tr>{}</tr></table>'.format(sizes, quantity))

        return '-'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'is_visible', 'add_to_main_page',)
    filter_horizontal = ('products',)

    def quantity(self, obj):
        return len(obj.products.all())


class SaleProductsInline(admin.TabularInline):
    model = SaleProducts
    extra = 1


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    inlines = (SaleProductsInline,)

    list_display = ('title', 'is_started',)

    def is_started(self, obj):
        return obj.is_started()
    is_started.boolean = True
