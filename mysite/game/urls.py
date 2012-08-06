from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('game.views',
	url(r'^$', 'index'),
	url(r'^(?P<patient_id>\d+)/$', 'detail'),
	url(r'^(?P<patient_id>\d+)/investigate/$', 'investigate'),
	url(r'^(?P<patient_id>\d+)/treat/$', 'treat'),
	url(r'^logout/$', 'logout_user')
)