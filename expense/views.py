'''Expense views implementation.'''


from django.shortcuts import redirect, render

from . import forms, models


def new_budget(request):
    '''Create new budget.'''
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
    '''Create new reimburse.'''
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
    '''List all requests.'''
    pass


def list_budgets(request):
    '''List all budgets from active user.'''
    budgets = models.Budget.objects.filter(requester=request.user)
    data = {
        'title': 'Meus pedidos de verba',
        'requests': models.get_as_request_data(budgets)
    }
    return render(request, 'request_list.html', data)


def list_reimburses(request):
    '''List all reimburses from active user.'''
    reimburses = models.Reimburse.objects.filter(requester=request.user)
    data = {
        'title': 'Meus pedidos de reembolso',
        'requests': models.get_as_request_data(reimburses)
    }
    return render(request, 'request_list.html', data)


def list_approvals(request):
    '''List all approvals.'''
    pass


def list_budget_approvals(request):
    '''List budget approvals.'''
    pass


def list_reimburse_approvals(request):
    '''List reimburse approvals.'''
    reimburses = models.Reimburse.objects.filter(approval=None)
    data = {
        'title': 'Aprovações de reembolso',
        'sections':[{
            'title': 'Pendentes',
            'requests': models.get_as_request_data(reimburses)
        }]
    }
    return render(request, 'approval_list.html', data)


def show_request(request, request_id):
    '''Show request page.'''
    pass
