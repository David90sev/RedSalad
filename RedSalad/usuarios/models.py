# -*- coding: utf-8 -*-
    
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import os
from django.db.models.fields.files import ImageField
from tkinter.filedialog import dialogstates


# Create your models here.
PROVINCIAS = (
    ('CO','A Coruña'),
    ('VI','�lava'),
    ('AB','Albacete'),
    ('AL','Alicante'),
    ('AM','Almer�a'),
    ('AS','Asturia'),
    ('AV','�vila'),
    ('BA','Badajoz'),
    ('BL','Baleares'),
    ('BR','Barcelona'),
    ('BU','Burgos'),
    ('CC','C�ceres'),
    ('CA','C�diz'),
    ('CN','Cantabria'),
    ('CS','Castell�n'),
    ('CR','Ciudad Real'),
    ('CO','C�rdoba'),
    ('CU','Cuenca'),
    ('GI','Girona'),
    ('GR','Granada'),
    ('GU','Guadalajara'),
    ('SS','Gipuzkoa'),
    ('HU','Huelva'),
    ('HU','Huesca'),
    ('JA','Ja�n'),
    ('LO','La Rioja'),
    ('GC','Las Palmas'),
    ('LE','Le�n'),
    ('LL','Lleida'),
    ('LU','Lugo'),
    ('MD','Madrid'),
    ('MA','M�laga'),
    ('MU','Murcia'),
    ('NA','Navarra'),
    ('OR','Ourense'),
    ('PA','Palencia'),
    ('PO','Pontevedra'),
    ('SA','Salamanca'),
    ('TF','Tenerife'),
    ('SG','Segovia'),
    ('SE','Sevilla'),
    ('SO','Soria'),
    ('TA','Tarragona'),
    ('TE','Teruel'),
    ('TO','Toledo'),
    ('VA','Valencia'),
    ('VL','Valladolid'),
    ('BI','Bizkaia'),
    ('ZA','Zamora'),
    ('ZR','Zaragoza'),
)


def get_image_path(instance, filename):
    return os.path.join('fotos', str(instance.id), filename)

# Usuario
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #comentario_blog
    #sender_m
    receiver_m = models.ForeignKey('Mensaje', on_delete=models.CASCADE)
    ###############################
    telefono = models.CharField(max_length=15)
    pais=models.CharField(max_length=20)
    ciudad=models.CharField(max_length=30)
    provincia = models.CharField(max_length=2, choices=PROVINCIAS)
    codigo_postal=models.CharField(max_length=10)
    direccion=models.CharField(max_length=30)
    foto=ImageField(upload_to=get_image_path, blank=True, null=True)
    fondo=ImageField(upload_to=get_image_path, blank=True, null=True)
    
    def __str__(self):
            return self.user.username+"-usuario-"
      
    
#class Cliente(models.Model):
class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #productor_seguido
    #comentario_perfil
    #comentario_producto
    #carrito
    ###################
    
    def __str__(self):              
        return "cliente:"+self.usuario
    
#class Productor(models.Model):
class Productor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #entrada_blog
    #comentario_perfil
    #catalogo
    #punto_de_distribucion
    seguidor = models.ForeignKey(Cliente)
    bio = models.CharField(max_length=500)
    
    def __str__(self):              
        return "productor:"+self.usuario
    
#class Admin(models.Model):
class Administrador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ############################
    
    def __str__(self):              
        return "administrador:"+self.usuario
    
    
class Mensaje(models.Model):
    sender_m =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #receiver_m
    ############################
    titulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1500)
    fecha = models.DateTimeField()
    visto = models.BooleanField()
    
    def __str__(self):              
        return "mensaje de "+self.sender_m+" fecha:"+self.fecha
    
## Solo un cliente puede comentar el perfil de un productor
class Comentario_perfil(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ##############################
    cuerpo = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    
    def __str__(self):              
        return "comentario de perfil de "+self.cliente +"a "+self.productor
    
