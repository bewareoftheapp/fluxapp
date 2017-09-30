from .models import Budget, Reimburse

from django.forms import ModelForm


class BudgetForm(ModelForm):
    '''Form for expense.models.Budget model.'''

    class Meta:  # pylint: disable=missing-docstring
        model = Budget
        fields = [
            'value',
            'description',
        ]


class ReimburseForm(ModelForm):
    '''Form for expense.models.Reimburse model.'''

    class Meta:  # pylint: disable=missing-docstring
        model = Reimburse
        fields = [
            'value',
            'description',
        ]
