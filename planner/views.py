from users import forms
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from .models import Ticket, Projeto
from .forms import NovoTicketForm, UpdateTicketForm, NovoProjetoForm, UpdateProjetoForm

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'planner/lista_ticket.html'
    paginate_by = 10
    ordering = ('-dt_inicio')

class NovoViewTicket(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = NovoTicketForm
    template_name = 'planner/novo_ticket.html'
    success_url = '/planner/tickets/'
    login_url = 'login'

    # Função para setar o usuário logado como criador
    def form_valid(self, form):
            form.instance.criado_por = self.request.user
            # form.instance.progresso = 'Novo'
            return super().form_valid(form)

class UpdateViewTicket(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = UpdateTicketForm
    template_name = 'planner/update_ticket.html'
    success_url = '/planner/tickets/'
    login_url = 'login'

    # Método para obter a instancia do objeto anterior e setar o novo progresso
    def form_valid(self, form):
        instance = self.get_object()
        progresso_old = instance.progresso_id
        progresso_novo = form.instance.progresso_id

        if progresso_old != progresso_novo and progresso_novo == 5:
            form.instance.dt_fim = timezone.now()
            form.instance.dt_atualizacao = timezone.now()
        return super().form_valid(form)

class DeleteViewTicket(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('lista-ticket')
    login_url = 'login'
    http_method_names = ["post"]

class DetailViewTicket(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'planner/detalhe_ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProjetosListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'planner/lista_projeto.html'
    paginate_by = 10
    ordering = ('-dt_inicio')

class NovoViewProjeto(LoginRequiredMixin, CreateView):
    model = Projeto
    form_class = NovoProjetoForm
    template_name = 'planner/novo_projeto.html'
    success_url = '/planner/projetos/'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.responsavel = self.request.user
        form.instance.status = 0
        return super().form_valid(form)

class UpdateViewProjeto(LoginRequiredMixin, UpdateView):
    model = Projeto
    form_class = UpdateProjetoForm
    template_name = 'planner/update_projeto.html'
    success_url = '/planner/projetos/'
    login_url = 'login'

    # Método para obter a instancia do objeto anterior e setar o novo status
    def form_valid(self, form):
        instance = self.get_object()
        status_old = instance.status
        status_novo = form.instance.status

        if status_old != status_novo and status_novo == 1:
            form.instance.dt_fim = timezone.now()
            form.instance.dt_atualizacao = timezone.now()
        return super().form_valid(form)

class DeleteViewProjeto(LoginRequiredMixin, DeleteView):
    model = Projeto
    success_url = reverse_lazy('lista-projeto')
    url_login = 'login'
    http_method_names = ['post']

class DetailViewProjeto(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = 'planner/detalhe_projeto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['projeto_ticket'] = Ticket.objects.filter(projeto_ticket__titulo = self.object)
        return context
