"""nao possievl lancar data de transacao pra um dia pra tras ou pra frente"""

from datetime import date
from django.core.exceptions import ValidationError
from django.utils import timezone


def valida_data(data):
    data_transacao = data.year
    data_atual = timezone.now().date().year
    if data_transacao <= data_atual - 1 or data_transacao >= data_atual + 1:
        raise ValidationError('Data não pode ser maior que o ano atual')
