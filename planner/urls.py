from django.urls import path
from .views import DeleteViewProjeto, NovoViewTicket, UpdateViewTicket, DeleteViewTicket, TicketListView, ProjetosListView, NovoViewProjeto, UpdateViewProjeto, DetailViewTicket, DetailViewProjeto

urlpatterns = [
    path('tickets/', TicketListView.as_view(), name='lista-ticket'),
    path('tickets/criar/', NovoViewTicket.as_view(), name='novo-ticket'),
    path('tickets/editar/<int:pk>', UpdateViewTicket.as_view(), name='editar-ticket'),
    path('tickets/excluir/<int:pk>', DeleteViewTicket.as_view(), name='excluir-ticket'),
    path('tickets/detalhes/<int:pk>', DetailViewTicket.as_view(), name='detalhe-ticket'),
    path('projetos/', ProjetosListView.as_view(), name='lista-projeto'),
    path('projetos/criar/', NovoViewProjeto.as_view(), name='novo-projeto'),
    path('projetos/editar/<int:pk>', UpdateViewProjeto.as_view(), name='editar-projeto'),
    path('projetos/excluir/<int:pk>', DeleteViewProjeto.as_view(), name='excluir-projeto'),
    path('projetos/detalhes/<int:pk>', DetailViewProjeto.as_view(), name='detalhe-projeto'),
]
