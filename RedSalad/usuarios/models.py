from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

  
#class Productor(models.Model):
class Productor(models.Model):
    
    
    
    
    NIF = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    pais
    ciudad
    provincia = models.CharField(max_length=2, choices=PROVINCIAS)
    codigo_postal
    direccion
    foto
    fondo
    
    
#class Cliente(models.Model):
class Cliente(models.Model):
    telefono = models.CharField(max_length=30)
    pais
    ciudad
    provincia
    codigo_postal
    direccion
    foto
    fondo
    
#class Admin(models.Model):

PROVINCIAS = (
    ('CO','A Coruña'),
    ('VI','Álava'),
    ('AB','Albacete'),
    ('AL','Alicante'),
    ('AM','Almería'),
    ('AS','Asturia'),
    ('AV','Ávila'),
    ('BA','Badajoz'),
    ('BL','Baleares'),
    ('BR','Barcelona'),
    ('BU','Burgos'),
    ('CC','Cáceres'),
    ('CA','Cádiz'),
    ('CN','Cantabria'),
    ('CS','Castellón'),
    ('CR','Ciudad Real'),
    ('CO','Córdoba'),
    ('CU','Cuenca'),
    ('GI','Girona'),
    ('GR','Granada'),
    ('GU','Guadalajara'),
    ('SS','Gipuzkoa'),
    ('HU','Huelva'),
    ('HU','Huesca'),
    ('JA','Jaén'),
    ('LO','La Rioja'),
    ('GC','Las Palmas'),
    ('LE','León'),
    ('LL','Lleida'),
    ('LU','Lugo'),
    ('MD','Madrid'),
    ('MA','Málaga'),
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
    
    
    
