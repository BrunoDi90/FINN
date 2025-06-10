from django.core.exceptions import ValidationError


def valida_descricao(descricao):
    if len(descricao) < 3 :
        raise ValidationError('Descricao tem q ter pelo menos 3 caracteres.')

    if isinstance(descricao, int):
        raise ValidationError('Descricao nao pode ser inteiro.')


