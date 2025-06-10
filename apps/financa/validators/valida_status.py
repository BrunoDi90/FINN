from django.core.exceptions import ValidationError


def valida_status(status):
    lista = ['E', 'P']

    if status not in lista:
        raise ValidationError('Status invalido')