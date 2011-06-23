from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^(?P<soap_id>\d+)/$', show, name="show"),
    url(r'^new/$', new, name="new"),
)

