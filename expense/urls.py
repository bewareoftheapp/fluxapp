'''URL routing for expense app.'''


from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^nova-verba/', views.new_budget, name='new_budget'),
    url(r'^novo-reembolso/', views.new_reimburse, name='new_reimburse'),
    url(r'verbas/', views.list_budgets, name='list_budgets'),
    url(r'reembolsos/', views.list_reimburses, name='list_reimburses'),
    url(r'aprovacoes/verba/', views.list_budget_approvals, name='list_budget_approvals'),
    url(r'aprovacoes/reembolso/', views.list_reimburse_approvals, name='list_reimburse_approvals'),
    url(r'requisicao/(?P<request_id>[0-9]+)/(?P<approval>(aprovar|negar){1})/', views.set_approval,
        name='set_approval'),
    url(r'requisicao/(?P<request_id>[0-9]+)/', views.show_request, name='show_request')
]
