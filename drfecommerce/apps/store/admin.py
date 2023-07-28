from django.contrib import admin
from .models import Brand, Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "parent",
        "name",
        "description",
        "photo",
        "slug",
        "is_featured",
        "ordering",
    )
    search_fields = ("name", "parent__name")
    readonly_fields = ("photo_preview",)
    list_filter = ("is_featured",)

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = "Photo Preview"
    photo_preview.allow_tags = True


CategoryAdmin.search_help_text = "Search By Name or Parent"
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Product)
