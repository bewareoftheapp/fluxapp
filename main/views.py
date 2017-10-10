'''Main views.'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse

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


def handler404(request):
    '''Handle not found errors.'''
    data = {
        'err_msg': 'Não consegui encontrar a página que você quer :(',
        'btn_msg': 'Voltar para a página inicial',
        'btn_href': reverse('index')
    }
    return render(request, 'oops.html', data)


def handler500(request):
    '''Handle generic server errors.'''
    data = {
        'err_msg': 'Não consegui fazer o que você me pediu :(',
        'btn_msg': 'Voltar para a página inicial',
        'btn_href': reverse('index')
    }
    return render(request, 'oops.html', data)
