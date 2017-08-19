from . import forms


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
