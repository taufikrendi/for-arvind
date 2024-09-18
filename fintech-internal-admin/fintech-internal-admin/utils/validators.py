import datetime
import os

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

numeric = RegexValidator(r'^[1-9+]', 'Only digit characters.')


def get_user(request):
    user = request.user.id
    return user


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]


def file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File yang anda unggah tidak berekstensi tipe atau .jpeg .jpg')


def file_size_image(value):
    limit = 1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File yang anda unggah Terlalu Besar, Ukuran Maksimal adalah 1MB.')