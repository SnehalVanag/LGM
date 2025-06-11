from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product

admin.site.register(CustomUser, UserAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount']
    fields = ['name', 'image', 'discount']