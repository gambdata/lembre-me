from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Ticket, SubTicket
from .forms import NovoTicketForm, UpdateTicketForm, NovoSubTicketForm

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'planner/lista_ticket.html'
    paginate_by = 3

class ProjetosListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'planner/deck_projetos.html'
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
            # form.instance.progresso = 'Novo'
            return super().form_valid(form)

class NovoViewSubTicket(LoginRequiredMixin, CreateView):
    model = SubTicket
    form_class = NovoSubTicketForm
    template_name = 'planner/novo_subticket.html'
    success_url = '/planner/'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.status = 0
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

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse('excluir-ticket', kwargs={'pk': self.object.pk})
            )
