from rest_framework import serializers
from pago_predial import models as m

class AdeudoSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.Adeudo
        fields = ['predio','ejercicio','subtotal','impuesto_adicional','recargo','multa','estatus_pago','estatus_descuento','total']

class DescuentoAdeudoSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.DescuentoAdeudo
        fields = ['id_adeudo','d_subtotal','d_recargo','d_multa']

class InformacionPagoSerializer(serializers.ModelSerializer):
    class Meta():
        model = m.InformacionPago
        fields = ['folio','id_adeudo','contribuyente','fecha','fecha','cajero']
