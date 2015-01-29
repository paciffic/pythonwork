from django.conf.urls import patterns, include, url
from django.contrib import admin
from pip._vendor.requests.packages.urllib3.util.timeout import current_time
from javis.views import current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'javis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
)
