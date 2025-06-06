from django.urls import path
from .views import NovoViewTicket, UpdateViewTicket, DeleteViewTicket

urlpatterns = [
    path('criar/', NovoViewTicket.as_view(), name='novo-ticket'),
    path('editar/<pk>', UpdateViewTicket.as_view(), name='editar-ticket'),
    path('excluir/<pk>', DeleteViewTicket.as_view(), name='excluir-ticket'),
]
