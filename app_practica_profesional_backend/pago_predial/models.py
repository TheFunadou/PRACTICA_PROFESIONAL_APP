from django.db import models
from user.models import Predio,Contribuyente
from django.contrib.auth.models import User

class Adeudo(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    ejercicio = models.CharField(max_length=4)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    impuesto_adicional = models.DecimalField(max_digits=10,decimal_places=2)
    recargo = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    multa = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estatus_pago = models.CharField(max_length=30)
    estatus_descuento = models.CharField(max_length=30, default='NO SOLICITADO')
    total = models.DecimalField(max_digits=10,decimal_places=2)

class DescuentoAdeudo(models.Model):
    id_adeudo = models.ForeignKey(Adeudo, on_delete=models.CASCADE)
    d_subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    d_recargo = models.DecimalField(max_digits=10,decimal_places=2)
    d_multa = models.DecimalField(max_digits=10,decimal_places=2)

class InformacionPago(models.Model):
    folio = models.BigAutoField(primary_key=True)
    id_adeudo = models.ForeignKey(Adeudo,on_delete=models.CASCADE)
    contribuyente = models.ForeignKey(Contribuyente,on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cajero = models.ForeignKey(User, on_delete=models.CASCADE)