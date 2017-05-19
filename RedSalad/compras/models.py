from django.db import models
from usuarios.models import Cliente
from ventas.models import Producto, Horario

# Create your models here.
class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField()
    comprado = models.BooleanField(default=False);

class Linea(models.Model):
    carrito= models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto)
    horario = models.ForeignKey(Horario)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    comprado = models.BooleanField(default=False)