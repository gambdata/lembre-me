from django.contrib import admin

from .models import Ticket, Progresso

class CustomPlannerAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['titulo', 'dt_inicio', 'progresso', 'responsavel']

admin.site.register(Ticket, CustomPlannerAdmin)
admin.site.register(Progresso)
