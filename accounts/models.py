from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator



def validate_iranian_nat_id(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Invalid Iranian national ID.')


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
