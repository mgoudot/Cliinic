# This also imports the include function
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls')),
    url(r'^game/login/$', 'django.contrib.auth.views.login', {'template_name': 'game/auth.html'}),
)
