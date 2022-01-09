from django.contrib import admin
from soldados.models import Arma, Soldado

# Register your models here.
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre')

class SoldadoAdmin(admin.ModelAdmin):
    list_display = ('apodo', 'estado', 'arma')

admin.site.register(Arma, ArmaAdmin)
admin.site.register(Soldado, SoldadoAdmin)