from django.contrib import admin
from products.models import CategoryModel, ProductModel

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":('name',)}

admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel)