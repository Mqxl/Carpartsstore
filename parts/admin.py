from django.contrib import admin

from .models import Category,Product, Slider,Profile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}   
admin.site.register(Product, ProductAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

admin.site.register(Slider, SliderAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
    
admin.site.register(Profile, ProfileAdmin)
