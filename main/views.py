from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from expense.models import Budget, Reimburse


@login_required
def index(request):
    '''Render index page.'''
    budgets = Budget.objects.filter(approval=None)
    reimburse = Reimburse.objects.filter(approval=None)
    user = request.user
    data = {'user': request.user,
            'my_pending_budget_count': budgets.filter(requester=user).count(),
            'my_pending_reimburse_count': reimburse.filter(requester=user).count()}
    if request.user.is_staff:
        data['pending_budget_count'] = budgets.count()
        data['pending_reimburse_count'] = reimburse.count()
    return render(request, 'index.html', data)
