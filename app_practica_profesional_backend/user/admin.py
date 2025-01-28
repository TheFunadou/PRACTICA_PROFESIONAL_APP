from django.contrib import admin
from user import models as m

# Register your models here.
admin.site.register(m.UserNotes)
admin.site.register(m.Contribuyente)
admin.site.register(m.Contacto)
admin.site.register(m.Predio)
admin.site.register(m.InformacionPredio)