from django.core.exceptions import ValidationError


def valida_descricao(descricao):
    if len(descricao):
        raise ValidationError('Descricao tem q ter pelo menos 3 caracteres e não pode ser maior que 300.')

    if isinstance(descricao, int):
        raise ValidationError('Descricao nao pode ser inteiro.')


