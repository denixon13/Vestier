from django.contrib import admin
from .models import Producto, Categoria, Subcategoria, TipoAtributo, AtributoProducto

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'subcategoria', 'creado', 'actualizado')
    search_fields = ('nombre', 'categoria__nombre')
    readonly_fields = ('creado', 'actualizado')
    list_filter = ('subcategoria', 'creado','actualizado')

    def mostrar_categoria(self, obj):
        return obj.subcategoria.categoria.nombre
        mostrar_categoria.short_description = 'Categoría'

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado', 'actualizado')
    search_fields = ('nombre',)
    readonly_fields = ('creado', 'actualizado')
    list_filter = ('creado','actualizado')

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'creado', 'actualizado')
    search_fields = ('nombre', 'categoria__nombre')
    readonly_fields = ('creado', 'actualizado')
    list_filter = ('categoria', 'creado','actualizado')

class TipoAtributoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad')
    search_fields = ('nombre',)

class AtributoProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo_atributo', 'valor', 'stock')
    search_fields = ('producto__nombre', 'tipo_atributo__nombre')
    list_filter = ('tipo_atributo',)



admin.site.register(Producto, ProductAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(TipoAtributo, TipoAtributoAdmin)
admin.site.register(AtributoProducto, AtributoProductoAdmin)
