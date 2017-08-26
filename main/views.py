from expense.models import Budget, Reimburse

from django.shortcuts import render, redirect


def user_index(request):
    budgets = Budget.objects.filter(approval=None)
    reimburse = Reimburse.objects.filter(approval=None)
    user = request.user
    data = {'user': request.user,
            'my_pending_budget_count': budgets.filter(requester=user).count(),
            'my_pending_reimburse_count': reimburse.filter(requester=user)
                .count()}
    if request.user.is_staff:
        data['pending_budget_count'] = budgets.count()
        data['pending_reimburse_count'] = budgets.count()
    return render(request, 'index.html', data)

def index(request):
    if request.user.is_authenticated():
        result = user_index(request)
    else:
        result = redirect('login')
    return result
