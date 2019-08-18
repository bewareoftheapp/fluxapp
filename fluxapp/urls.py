'''Register fluxapp urls routes.'''

import user.urls
import user.views

from django.conf.urls import include, url
from django.contrib import admin

import expense.urls
import main.views

admin.autodiscover()

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

urlpatterns = [
    url(r'^dump/', main.views.dump, name='dump'),
    url(r'^$', main.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', user.views.login_page, name='login'),
    url(r'^logout/', user.views.logout_user, name='logout'),
    url(r'^financeiro/', include(expense.urls)),
    url(r'^usuario/', include(user.urls)),
]
