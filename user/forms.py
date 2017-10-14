'''User forms.'''
# pylint: disable=too-few-public-methods

from django import forms
from django.contrib.auth.models import User

from .models import RegistrationToken


class RegistrationTokenForm(forms.ModelForm):
    '''Form for user.models.RegistrationToken model.'''

    class Meta:  # pylint: disable=missing-docstring
        model = RegistrationToken
        fields = [
            'email',
        ]
        labels = {
            'email': 'e-mail'
        }
        error_messages = {
            'email': {
                # pylint: disable=line-too-long
                'required': 'Por favor, preencha o campo de e-mail com o e-mail do usuário a ser adcionado.',
                'invalid': 'Oops, parece que esse e-mail está escrito errado. :('
            }
        }


class UserForm(forms.ModelForm):
    '''Form for user registration.'''

    class Meta:  #pylint: disable=missing-docstring
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'password': 'Senha'
        }
        error_messages = {
            'username': {
                'required': 'Por favor, informe um nome de usuário.',
                'unique': 'Este nome de usuário já existe.'
            },
            'first_name': {
                'required': 'Por favor, nos diga qual o seu nome.'
            },
            'last_name': {
                'required': 'Por favor, nos diga qual o seu sobrenome.'
            },
            'email': {
                'required': 'Precisamos saber o seu e-mail.'
            },
            'password': {
                'required': 'Precisamos de senha para sua conta.'
            }
        }
        help_texts = {
            'username': None
        }
