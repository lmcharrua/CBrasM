from django.contrib import admin
from .models import Clientes, Tratamento, Exames

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Tratamento)
admin.site.register(Exames)