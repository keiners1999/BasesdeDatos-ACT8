from django.contrib import admin
from apps.ventas.models import Venta, VehiculoVenta

# Register your models here.


class NembershipInline(admin.TabularInline):
    model = VehiculoVenta
    extra = 1
    
class VentaAdmin(admin.ModelAdmin):
    inlines = (NembershipInline, )
    
admin.site.register(Venta, VentaAdmin)
