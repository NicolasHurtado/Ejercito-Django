from django.contrib import admin
from soldados.models import Arma, Soldado, HistorialSoldado

# Register your models here.
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre')

class SoldadoAdmin(admin.ModelAdmin):
    list_display = ('apodo', 'estado', 'arma')

class HistorialAdmin(admin.ModelAdmin):
    list_display = ('soldado', 'arma')

admin.site.register(Arma, ArmaAdmin)
admin.site.register(Soldado, SoldadoAdmin)
admin.site.register(HistorialSoldado, HistorialAdmin)