from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Usuario

PROGRESS = [
    ('0', 'Novo'),
    ('1', 'Em andamento'),
    ('2', 'Pendente'),
    ('3', 'Cancelado'),
    ('4', 'Concluído')
]

class Ticket(models.Model):
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_criados')
    titulo = models.CharField(_('Título'), max_length=50, null=False)
    conteudo = models.TextField(_('Conteúdo'))
    progresso = models.CharField(_('Progresso'), max_length=1, choices=PROGRESS, default='0')
    dt_inicio = models.DateTimeField(_('Data início'), auto_now_add=True)
    dt_fim = models.DateTimeField(_('Data fim'), blank=True, null=True)
    dt_conclusao_prev = models.DateTimeField(_('Data conclusão prevista'), blank=True, null=True)
    dt_atualizacao = models.DateTimeField(_('Data atualização'), auto_now=True)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tickets_designados')

    def __str__(self):
        return self.titulo
