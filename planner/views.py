from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ticket
from .forms import NovoTicketForm, UpdateTicketForm

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'planner/lista_ticket.html'
    paginate_by = 10

class NovoViewTicket(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = NovoTicketForm
    template_name = 'planner/novo_ticket.html'
    success_url = '/planner/'
    login_url = 'login'

    # Função para setar o usuário logado como criador
    def form_valid(self, form):
            form.instance.criado_por = self.request.user
            return super().form_valid(form)

class UpdateViewTicket(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = UpdateTicketForm
    template_name = 'planner/ticket_update_form.html'
    success_url = '/planner/'
    login_url = 'login'

class DeleteViewTicket(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('lista-ticket')
    login_url = 'login'
