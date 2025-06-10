from django.urls import path
from .views import NovoViewSubTicket, NovoViewTicket, UpdateViewTicket, DeleteViewTicket, TicketListView, ProjetosListView

urlpatterns = [
    path('criar/', NovoViewTicket.as_view(), name='novo-ticket'),
    path('editar/<int:pk>', UpdateViewTicket.as_view(), name='editar-ticket'),
    path('excluir/<int:pk>', DeleteViewTicket.as_view(), name='excluir-ticket'),
    path('', TicketListView.as_view(), name='lista-ticket'),
    path('projetos/', ProjetosListView.as_view(), name='projetos-ticket'),
    path('criar_subticket/', NovoViewSubTicket.as_view(), name='novo-subticket'),
]
