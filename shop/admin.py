from django.contrib import admin
from .models import Products , Order
# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "ABC shopping"
admin.site.index_title = "Manage ABC shooping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_defalut(self,request,queryset):
        queryset.update(category='default',)

    change_category_to_defalut.short_description = "Default Category"

    list_display = ('title','price','discount_price','category','description',)
    search_fields = ('title',)
    actions = ('change_category_to_defalut',)
    fields = ('price','discount_price')
    list_editable = ('price','category')

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)