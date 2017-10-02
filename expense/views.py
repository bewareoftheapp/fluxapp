'''Expense views implementation.'''


from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


@login_required
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


@login_required
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


@login_required
def list_budgets(request):
    '''List all budgets from active user.'''
    budgets = models.Budget.objects.filter(requester=request.user)
    data = {
        'show_requester': False,
        'title': 'Meus pedidos de verba',
        'requests': models.get_as_request_data(budgets)
    }
    return render(request, 'request_list.html', data)


@login_required
def list_reimburses(request):
    '''List all reimburses from active user.'''
    reimburses = models.Reimburse.objects.filter(requester=request.user)
    data = {
        'show_requester': False,
        'title': 'Meus pedidos de reembolso',
        'requests': models.get_as_request_data(reimburses)
    }
    return render(request, 'request_list.html', data)


@staff_member_required(login_url='login')
def list_all_reimburses(request):
    '''List all reimburses.'''
    reimburses = models.Reimburse.objects.all()
    data = {
        'show_requester': True,
        'title': 'Todos os pedidos de reembolso',
        'requests': models.get_as_request_data(reimburses)
    }
    return render(request, 'request_list.html', data)


@staff_member_required(login_url='login')
def list_budget_approvals(request):
    '''List budget approvals.'''
    budgets = models.Budget.objects.filter(approval=None)
    data = {
        'title': 'Aprovações de verba',
        'sections':[{
            'title': 'Pendentes',
            'requests': models.get_as_request_data(budgets)
        }]
    }
    return render(request, 'approval_list.html', data)


@staff_member_required(login_url='login')
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


def get_request_or_404(request_id):
    '''Get a request and resolve it to budget or reimburse.'''
    req = get_object_or_404(models.Request, pk=request_id)
    try:
        return req.reimburse
    except models.Reimburse.DoesNotExist:
        return req.budget


@login_required
def show_request(request, request_id):
    '''Show request page.'''
    req = get_request_or_404(request_id)
    data = {
        'request': models.RequestData(req),
        'user': request.user
    }

    if request.method == "POST" and request.POST['text']:
        req.commentary_set.create(author=request.user, text=request.POST['text'])

    return render(request, 'request.html', data)


@staff_member_required(login_url='login')
def set_approval(request, request_id, approval):
    '''Set approval for request.'''
    req = get_object_or_404(models.Request, pk=request_id)
    approval_status = approval == 'aprovar'
    req.approval_set.create(approver=request.user, status=approval_status)
    return redirect('show_request', request_id=request_id)
