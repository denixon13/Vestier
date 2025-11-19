from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/<int:atributo_id>/', views.agregar_producto, name='agregar'),
    path('agregar-desde-formulario/<int:producto_id>/', views.agregar_desde_formulario, name='agregar_desde_formulario'),
    path('eliminar/<int:producto_id>/<int:atributo_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
]