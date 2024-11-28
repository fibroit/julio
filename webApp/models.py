from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
# Modelo para Categorías de Ropa (e.g., Camisas, Pantalones, Accesorios)
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()  # Cantidad en inventario
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    color = models.CharField(max_length=50, blank=True, null=True)  # Color del producto
    talla = models.CharField(max_length=10, blank=True, null=True)  # Talla o tamaño del producto
    disponible = models.BooleanField(default=True)  # Si el producto está disponible o no
    fecha_agregado = models.DateTimeField(auto_now_add=True)  # Fecha en que se agregó el producto
    fecha_actualizado = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    def __str__(self):
        return self.nombre

# Modelo para Órdenes de Compra
class Orden(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ordenes")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completada', 'Completada'), ('cancelada', 'Cancelada')])

    def __str__(self):
        return f"Orden {self.id} - {self.username.username}"
    
   

