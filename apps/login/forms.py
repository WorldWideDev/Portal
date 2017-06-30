from django.forms import ValidationError, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import Instructor
from django.core import validators

class NameField(CharField):
    MIN_LENGTH = 2
    NAME_REGEX = r'^[a-zA-Z]+$'
    NameMinLengthValidator = validators.MinLengthValidator(
        MIN_LENGTH,
        "Name Fields must be %(limit_value)d or more characters long, you have %(show_value)d"
    )
    NameRegexValidator = validators.RegexValidator(
        NAME_REGEX,
        "Names must only contain letter characters"
    )
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)
        self.validators.append(NameField.NameMinLengthValidator)
        self.validators.append(NameField.NameRegexValidator)

class RegistrationForm(UserCreationForm):

    first_name = NameField()
    last_name = NameField()

    password1 = CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control'
        }),
        label="Password"
    )
    password2 = CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control'
        }),
        label="Confirm Password"
    )

    class Meta:
        model = Instructor
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]