from . import views


from django.conf.urls import url


urlpatterns = [
    url(r'^nova-verba/', views.new_budget, name='new_budget'),
    url(r'^novo-reembolso/', views.new_reimburse, name='new_reimburse'),
    url(r'verbas/', views.list_budgets, name='list_budgets'),
    url(r'reembolsos/', views.list_reimburses, name='list_reimburses'),
]
