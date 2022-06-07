from django.contrib import admin
from .models import Category, Product, Book, Magazine, Record
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Record)