from django.contrib import admin

from product.models import Category, Product

#TODO: реализовать загрузку несколько изображении
class ProductImageInline(admin.TabularInlibe):
    model = ProductImage
    readonly_ fields = ['image',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links =  ['id',' name']
    list_filter = ['category']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)