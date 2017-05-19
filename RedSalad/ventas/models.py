from django.db import models
from usuarios.models import Productor, Cliente
from test.test_sys_settrace import called

DIAS = (
    ('LU','Lunes'),
    ('MA','Martes'),
    ('MI','Miercoles'),
    ('JU','Jueves'),
    ('VI','Viernes'),
    ('SA', 'Sabado'),
    ('DO', 'Domingo'),
    )

# Create your models here.
class Catalogo(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    #########################
    titulo = models.CharField(max_length=20)

class Producto(models.Model):
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    #########################
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    existencias = models.BooleanField()
    fecha_publicacion = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
class Comentario_producto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #########################
    cuerpo = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    
class Punto_Distribucion(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    coordenada = models.CharField(max_length=100)
    
class Horario(models.Model):
    punto_distribucion = models.ForeignKey(Punto_Distribucion, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    dia = models.CharField(max_length=2, choices=DIAS)

