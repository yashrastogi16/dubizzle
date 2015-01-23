from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dubizzle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^uberhomes/api/dubizzle/daily/daily.xml', 'api.views.daily', name='daily'),
    url(r'^uberhomes/api/dubizzle/hourly/hourly.xml','api.views.hourly',name='hourly'),
    url(r'^uberhomes/api/propertyfinder/feed.xml','api.views.feed',name='feed'),
)
