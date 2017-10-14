'''Department forms.'''
# pylint: disable=too-few-public-methods

from django import forms

from .models import Department


class DepartmentForm(forms.ModelForm):
    '''Form for department.models.Department model.'''

    class Meta:  #pylint: disable=missing-docstring
        model = Department
        fields = [
            'name'
        ]
