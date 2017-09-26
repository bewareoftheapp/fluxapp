'''Register user url routes.'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^novo/', views.new_user, name='new_user'),
    url(r'^registrar/', views.register_user, name='register_user')
]
