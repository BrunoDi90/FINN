from django.core.exceptions import ValidationError


def valida_valor(valor):

    if valor <= 0:
        raise ValidationError('Valor tem q ser maior que 0')