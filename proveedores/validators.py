
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validacion_alfanumerica(value):
    if not value.isalnum():
        raise ValidationError(
            _('%(value)s Solo acepta letras y numeros'),
            params={'value': value},
        )