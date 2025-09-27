from django.contrib import admin

# Register your models here.

from .models import Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio', 'stock', 'categoria')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
from .models import Categoria