from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[1-9+]', 'Only digit characters.')


def str2bool(v):
    return v.lower() in ("true", "True")