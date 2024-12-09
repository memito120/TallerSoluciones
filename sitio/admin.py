from django.contrib import admin
from sitio.models import Ticket

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'estado', 'creado', 'actualizado')
    list_filter = ('estado', 'creado')
    search_fields = ('descripcion', 'usuario__username')
