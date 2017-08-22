from . import views


from django.conf.urls import url


urlpatterns = [
    url(r'^nova-verba/', views.new_budget, name='new_budget'),
    url(r'^novo-reembolso', views.new_reimburse, name='new_reimburse'),
]