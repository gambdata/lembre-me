from django.contrib import admin

from .models import SubTicket, Ticket, Progresso

class CustomPlannerAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['titulo', 'dt_inicio', 'progresso', 'responsavel']
    list_filter = ['titulo', 'responsavel']

@admin.register(SubTicket)
class CustomPlannerSubTicket(admin.ModelAdmin):
    list_display = ['criado_por', 'titulo', 'status']
    list_filter = ['titulo']

admin.site.register(Ticket, CustomPlannerAdmin)
admin.site.register(Progresso)
