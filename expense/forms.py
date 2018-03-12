'''Forms for expense app.'''
from django.forms import ModelForm

from .models import Budget, Reimburse


class BudgetForm(ModelForm):
    '''Form for expense.models.Budget model.'''

    class Meta:  # pylint: disable=missing-docstring
        model = Budget
        fields = [
            'value',
            'description',
        ]
        labels = {
            'value': 'Valor',
            'description': 'Descrição'
        }


class ReimburseForm(ModelForm):
    '''Form for expense.models.Reimburse model.'''

    class Meta:  # pylint: disable=missing-docstring
        model = Reimburse
        fields = [
            'value',
            'description',
        ]
        labels = {
            'value': 'Valor',
            'description': 'Descrição'
        }
