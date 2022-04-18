from django.contrib import admin

from .models import *

admin.site.register(Room)
admin.site.register(Image)


class ProductImageAdmin(admin.ModelAdmin):
  pass


class ProductImageInline(admin.StackedInline):
  model = Image
  max_num = 10
  extra = 0


class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImageInline,]

