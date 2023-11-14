import re


def get_field_validation_type(value: str) -> str:
    """
    get_field_validation_type(value) -> str

    Определяет тип поля формы по значению
    """
    fields = {
        'date': r'^\d\d\.\d\d\.\d{4}$',
        'email': r'^\S+@\w+.\w{2,4}$',
        'phone': r'^\+7\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2}$',
    }
    for field_type, regex in fields.items():
        if re.fullmatch(regex, value):
            return field_type
    return 'text'


def get_form_validation_type(form: dict) -> dict:
    """
    get_form_validation_type(params) -> dict

    Определяет тип полей всей формы
    """
    field_validators = {}
    for field_name, field_value in form.items():
        validation_type = get_field_validation_type(field_value)
        field_validators[field_name] = validation_type
    return field_validators

