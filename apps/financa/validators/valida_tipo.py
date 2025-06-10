from django.core.exceptions import ValidationError


def valida_tipo(status):

    lista = ['R', 'D']

    if status not in lista:
        raise ValidationError('Tipo invalido')