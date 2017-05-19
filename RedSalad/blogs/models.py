from django.db import models
from usuarios.models import Productor, Usuario, get_image_path
from django.db.models.fields.files import ImageField

# Create your models here.
class Entrada_Blog(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    #comentarios
    ############################
    titulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=2500)
    imagen = ImageField(upload_to=get_image_path, blank=True, null=True)
    fecha = models.DateTimeField()

class Comentario_blog(models.Model):
    entrada_blog = models.ForeignKey(Entrada_Blog, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ############################
    cuerpo= models.CharField(max_length=150)
    fecha = models.DateTimeField()
    