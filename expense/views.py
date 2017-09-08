from . import forms
from . import models


from django.shortcuts import render, redirect


def new_budget(request):
    if request.method == "GET":
        data = {'budget_form': forms.BudgetForm()}
        result = render(request, 'new_budget.html', data)
    else:
        budget_form = forms.BudgetForm(request.POST)
        budget = budget_form.save(commit=False)
        budget.requester = request.user
        budget.save()
        result = redirect('index')

    return result


def new_reimburse(request):
    if request.method == "GET":
        data = {'reimburse_form': forms.ReimburseForm}
        result = render(request, 'new_reimburse.html', data)
    else:
        reimburse_form = forms.ReimburseForm(request.POST)
        reimburse = reimburse_form.save(commit=False)
        reimburse.requester = request.user
        reimburse.save()
        result = redirect('index')

    return result


def list_request(request):
    pass


def list_budgets(request):
    budgets = models.Budget.objects.filter(requester=request.user)
    data = {
        'title': 'Meus pedidos de verba',
        'requests': models.get_as_request_data(budgets)
    }
    return render(request, 'request_list.html', data)


def list_reimburses(request):
    reimburses = models.Reimburse.objects.filter(requester=request.user)
    data = {
        'title': 'Meus pedidos de reembolso',
        'requests': models.get_as_request_data(reimburses)
    }
    return render(request, 'request_list.html', data)
