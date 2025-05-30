from django.contrib import admin

from .models import Ticket

class CustomPlannerAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['titulo', 'dt_inicio', 'progresso', 'responsavel']

admin.site.register(Ticket, CustomPlannerAdmin)
