# from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from users.models import Usuario

User = get_user_model()

PROGRESSO = [
    ('1', 'Novo'),
    ('2', 'Em andamento'),
    ('3', 'Pendente'),
    ('4', 'Cancelado'),
    ('5', 'Concluído')
]

class Progresso(models.Model):
    progresso = models.CharField(_('Progresso'), max_length=20, default='Novo')

    def __str__(self):
        return self.progresso

class Ticket(models.Model):
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_criados')
    titulo = models.CharField(_('Título'), max_length=50, null=False)
    # progresso = models.CharField(_('Progresso'), max_length=1, choices=PROGRESSO, default='1')
    progresso = models.ForeignKey(Progresso, on_delete=models.CASCADE, related_name='ticket_progresso')
    dt_inicio = models.DateTimeField(_('Data início'), auto_now_add=True)
    dt_fim = models.DateTimeField(_('Data fim'), blank=True, null=True)
    dt_conclusao_prev = models.DateTimeField(_('Data conclusão prevista'), blank=True, null=True)
    dt_atualizacao = models.DateTimeField(_('Data atualização'), auto_now=True)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tickets_designados')

    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projeto_criado')
    titulo = models.CharField(_('Titulo'), max_length=50, null=False)
    descricao = models.TextField(_('Descrição'), blank=True, null=True)
    status = models.BooleanField(_('Status'), default=0)
    dt_inicio = models.DateTimeField(_('Data início'), auto_now_add=True)
    dt_fim = models.DateTimeField(_('Data fim'), blank=True, null=True)
    sub_ticket = models.ManyToManyField(Ticket, related_name='projeto_ticket')
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='projeto_designado')

    def __str__(self):
        return self.titulo
