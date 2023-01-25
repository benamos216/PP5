from django.contrib import admin
from .models import Stock, Category


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'stock_quantity',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Stock, StockAdmin)
admin.site.register(Category, CategoryAdmin)
