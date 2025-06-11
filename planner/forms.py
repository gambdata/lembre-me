from django import forms

from .models import Ticket, Projeto

class NovoTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo','progresso','dt_conclusao_prev','responsavel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'progresso': forms.Select(attrs={'class': 'form-control'}),
            'dt_conclusao_prev': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'})
        }

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo','progresso','dt_conclusao_prev','responsavel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'progresso': forms.Select(attrs={'class': 'form-control'}),
            'dt_conclusao_prev': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'})
        }

class NovoProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }

class UpdateProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo','descricao','status','sub_ticket','responsavel']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'sub_ticket': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'})
        }
