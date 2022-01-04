from django.contrib import admin
from .models import Fruit, Discount, Vegetable


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Discount, OfferAdmin)

admin.site.register(Fruit, FruitAdmin)

admin.site.register(Vegetable, VegetableAdmin)
