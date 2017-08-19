from .models import Budget, Reimburse

from django.forms import ModelForm


class BudgetForm(ModelForm):

    class Meta:
        model = Budget
        fields = [
            'value',
            'description',
        ]


class ReimburseForm(ModelForm):

    class Meta:
        model = Reimburse
        fields = [
            'value',
            'description',
        ]
