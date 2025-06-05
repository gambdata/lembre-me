from django import forms

from .models import Ticket

class NovoTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['criado_por','titulo','conteudo','dt_conclusao_prev','responsavel']
