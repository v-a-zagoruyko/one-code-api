from django.contrib import admin
from meta.models import Sizes


@admin.register(Sizes)
class SizesAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_module_permission(self, request):
        return False