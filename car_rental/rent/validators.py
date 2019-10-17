from django.core.exceptions import ValidationError



def validate_model(value):
    if value in {None, "", '{}', '[]', '()'}:
        raise ValidationError('{} is not a valid model name'.format(value))


def validate_model_is_not_digit(value):
    if value.isdigit() :
        raise ValidationError('it is a number, not a name'.format(value))
    if value.lstrip('-+').isdigit():
        raise ValidationError('it is a number, not a name'.format(value))


def validate_client_name(value):
    if value in {None, "", '{}', '[]', '()'}:
        raise ValidationError('{} is not a valid client_name'.format(value))


def validate_client_name_is_not_digit(value):
    if value.isdigit():
        raise ValidationError('it is a number, not a client_name'.format(value))
    if value.lstrip('-+').isdigit():
        raise ValidationError('it is a number, not a client_name'.format(value))


def validate_color(value):
    if value in {None, "", '{}', '[]', '()'}:
        raise ValidationError('{} is not a valid color'.format(value))


def validate_color_is_not_digit(value):
    if value.isdigit():
        raise ValidationError('it is a number, not a color'.format(value))
    if value.lstrip('-+').isdigit():
        raise ValidationError('it is a number, not a color'.format(value))