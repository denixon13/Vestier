from . import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', views.productos, name='all_products'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:categoria_id>/', views.categoria_detail, name='categoria_detail'),
    path('subcategorias/<int:subcategoria_id>/', views.subcategoria_detail, name='subcategoria_detail'),
    path('productos/<int:producto_id>/', views.producto_detail, name='producto_detail'),
    path('buscar/', views.buscar, name='buscar'),
]