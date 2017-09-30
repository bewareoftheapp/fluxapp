'''Register fluxapp urls routes.'''

import user.urls
import user.views

from django.conf.urls import include, url
from django.contrib import admin

import expense.urls
import main.views

admin.autodiscover()


# Examples:
# url(r'^$', 'fluxapp.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', user.views.login_page, name='login'),
    url(r'^logout/', user.views.logout_user, name='logout'),
    url(r'^financeiro/', include(expense.urls)),
    url(r'^usuario/', include(user.urls)),
]
