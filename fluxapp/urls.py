import main.views
import expense.urls
import user.views

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'fluxapp.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', user.views.login_page, name='login'),
    url(r'^logout/', user.views.logout_user, name='logout'),
    url(r'carteira/', include(expense.urls))
]
