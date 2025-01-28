from django.contrib import admin
from pago_predial import models as m
# Register your models here.
admin.site.register(m.Adeudo)
admin.site.register(m.DescuentoAdeudo)
admin.site.register(m.InformacionPago)