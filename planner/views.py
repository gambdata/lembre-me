from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ticket
from .forms import NovoTicketForm

User = get_user_model()

class NovoViewTicket(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = NovoTicketForm
    template_name = 'planner/novo_ticket.html'
    success_url = '/planner/'

class UpdateViewTicket(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['titulo','conteudo','progresso','dt_conclusao_prev','responsavel']
    template_name_suffix = '_update_form'
    success_url = '/'

class DeleteViewTicket(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('index')