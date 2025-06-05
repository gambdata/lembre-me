from django.urls import path
from .views import NovoViewTicket

urlpatterns = [
    path('criar/', NovoViewTicket.as_view(), name='novo-ticket'),
]
