from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
PROVINCIAS = (
    ('CO','A Coru�a'),
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
  
#class Productor(models.Model):
class Productor(models.Model): 
    NIF = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    pais =models.CharField(max_length=20)
    ciudad =models.CharField(max_length=30)
    provincia = models.CharField(max_length=2, choices=PROVINCIAS)
    codigo_postal =models.CharField(max_length=10)
    direccion= models.CharField(max_length=30)
    #foto
    #fondo
    
    
#class Cliente(models.Model):
class Cliente(models.Model):
    telefono = models.CharField(max_length=15)
    pais=models.CharField(max_length=20)
    ciudad=models.CharField(max_length=30)
    provincia = models.CharField(max_length=2, choices=PROVINCIAS)
    codigo_postal=models.CharField(max_length=10)
    direccion=models.CharField(max_length=30)
    #foto
    #fondo
    
#class Admin(models.Model):


    
    
    
