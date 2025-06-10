from django import forms

from .models import Ticket, SubTicket

class NovoTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo','conteudo','progresso','dt_conclusao_prev','responsavel']
        widgets = {
            # 'criado_por': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control'}),
            'progresso': forms.Select(attrs={'class': 'form-control'}),
            'dt_conclusao_prev': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'})
        }

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo','conteudo','progresso','dt_conclusao_prev','responsavel','subticket']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control'}),
            'progresso': forms.Select(attrs={'class': 'form-control'}),
            'dt_conclusao_prev': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            'subticket': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

class NovoSubTicketForm(forms.ModelForm):
    class Meta:
        model = SubTicket
        fields = ['titulo', 'status']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'})
        }
