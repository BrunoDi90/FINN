from django.db import models
from core.model import BaseModel
from apps.financa.validators.valida_data import valida_data
from apps.financa.validators.valida_tipo import valida_tipo
from apps.financa.validators.valida_status import valida_status
from apps.financa.validators.valida_descricao import valida_descricao
from apps.financa.validators.valida_valor import valida_valor

class Transacao(BaseModel):

    TIPO_CHOICES = (
        ('R', 'Receita'),
        ('D', 'Despesa')
    )

    STATUS_CHOICES = (
        ('E', 'Efetivado'),
        ('P', 'Pendente')
    )

    descricao = models.CharField(
        max_length=200,
        verbose_name='Descrição',
        help_text='descrição da transação',
        validators=[valida_descricao]
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Valor',
        help_text='valor da transação',
        validators=[valida_valor]
    )

    tipo_transacao = models.CharField(
        max_length=1,
        choices=TIPO_CHOICES,
        verbose_name='Tipo da transação',
        help_text='receita ou despesa',
        validators=[valida_tipo]
    )

    status_transacao = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name='Status da transação',
        help_text='Pendente ou Efetivado',
        validators=[valida_status]

    )

    data_transacao = models.DateField(
        verbose_name='Data da transação',
        help_text='xx/xx/xxxx',
        validators=[valida_data]
    )



    def __str__(self):
        return f'{self.descricao} - R$ {self.valor}'

    class Meta:
        verbose_name='Transação'
        verbose_name_plural='Transações'
        ordering = ['data_transacao']