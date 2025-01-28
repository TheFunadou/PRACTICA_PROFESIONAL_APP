from django.db import models
from django.contrib.auth.models import User

# User models
class UserNotes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.CharField(50)
    

# Create your models here.
# Contribuyente models
class Contribuyente(models.Model):
    rfc = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=25)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    correo = models.EmailField()


class Contacto(models.Model):
    numero_telefonico = models.CharField(max_length=10)
    contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15)
    
    class Meta:
        unique_together = (('numero_telefonico', 'contribuyente','tipo'),) 
    
class Predio(models.Model):
    clave_catastral = models.CharField(max_length=27,unique=True)
    contribuyente = models.ForeignKey(Contribuyente,on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    valor_catastral = models.DecimalField(max_digits=10,decimal_places=2)
    num_ext = models.CharField(max_length=5)
    num_int = models.CharField(max_length=5,default='N/A', blank=True)
    col_fracc = models.CharField(max_length=50)
    localidad = models.CharField(max_length=25,default='MINATITLAN')   
    codigo_postal = models.CharField(max_length=5)
    
class InformacionPredio(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=25)
    estado_fisico = models.CharField(max_length=25)
    superficie= models.DecimalField(max_digits=10,decimal_places=2)
    uso = models.CharField(max_length=25)
    antiguedad = models.PositiveSmallIntegerField()
    tenencia = models.CharField(max_length=25,default='N/A') 