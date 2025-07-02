from django.contrib import admin

from .models import Ticket, Progresso, Projeto

@admin.register(Ticket)
class CustomPlannerTicket(admin.ModelAdmin):
    list_display = ['titulo', 'dt_inicio', 'dt_fim', 'progresso', 'responsavel']
    list_filter = ['titulo', 'responsavel']

@admin.register(Projeto)
class CustomPlannerProjeto(admin.ModelAdmin):
    list_display = ['criado_por','titulo','dt_inicio','dt_fim','responsavel','status']
    list_filter = ['titulo']

admin.site.register(Progresso)
