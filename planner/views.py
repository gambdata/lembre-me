from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Ticket
from .forms import NovoTicketForm

class NovoViewTicket(CreateView):
    model = Ticket
    form_class = NovoTicketForm
    template_name = 'planner/novo_ticket.html'
    success_url = '/planner/'
