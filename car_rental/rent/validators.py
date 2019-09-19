from django.core.exceptions import ValidationError


def validate_model_name(value):
    if not value:
        raise ValidationError(
            '%(value)s cannot be empty',
            params={'value': value},
        )
