'''Register user url routes.'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^novo/', views.new_user, name='new_user'),
    url(r'^registrar/', views.register_user, name='register_user'),
    url(r'^convites/', views.active_tokens, name='active_tokens'),
    url(r'^administradores/', views.staff_users, name='staff_users')
]
