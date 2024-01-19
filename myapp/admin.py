from django.contrib import admin
from .models import Product , Customer , Order

# Register your models here.
#class ProductAdmin(admin.ModelAdmin):
    #list_display = ('field1', 'field2', 'field3')

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
