from django.urls import path
from .views import NovoViewTicket, UpdateViewTicket, DeleteViewTicket, TicketListView

urlpatterns = [
    path('criar/', NovoViewTicket.as_view(), name='novo-ticket'),
    path('editar/<int:pk>', UpdateViewTicket.as_view(), name='editar-ticket'),
    path('excluir/<int:pk>', DeleteViewTicket.as_view(), name='excluir-ticket'),
    path('', TicketListView.as_view(), name='lista-ticket'),
]
