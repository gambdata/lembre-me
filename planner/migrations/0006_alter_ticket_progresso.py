# Generated by Django 5.2 on 2025-06-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_alter_ticket_criado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='progresso',
            field=models.CharField(choices=[(1, 'Novo'), (2, 'Em andamento'), (3, 'Pendente'), (4, 'Cancelado'), (5, 'Concluído')], default=1, max_length=1, verbose_name='Progresso'),
        ),
    ]
