from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre', '-creado']

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='subcategorias/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['nombre', '-creado']
        unique_together = ('nombre', 'categoria')

    def __str__(self):
        return f"{self.categoria.nombre} - {self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, related_name='productos', blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre','-creado']

    def __str__(self):
        return self.nombre

class TipoAtributo(models.Model):
    nombre = models.CharField(max_length=50)  # Ej: Talla, Color, Capacidad
    unidad = models.CharField(max_length=20, blank=True, null=True)  # Ej: cm, GB, kg

    def __str__(self):
        return self.nombre
    
class AtributoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='atributos')
    tipo_atributo = models.ForeignKey(TipoAtributo, on_delete=models.CASCADE)
    valor = models.CharField(max_length=100)  # Ej: "M", "Rojo", "64"
    stock = models.PositiveIntegerField(default=0)  # Cantidad en inventario

    class Meta:
        unique_together = ('producto', 'tipo_atributo', 'valor')
        verbose_name = 'Atributo de Producto'
        verbose_name_plural = 'Atributos de Productos'

    def __str__(self):
        return f"{self.producto.nombre} - {self.tipo_atributo.nombre}: {self.valor}"
