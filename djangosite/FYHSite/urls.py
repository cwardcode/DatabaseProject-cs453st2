from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','FYHSite.site.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Games/(?P<game_id>\d+)/$', 'FYHSite.site.views.gamesdetail'),
    url(r'^Games/', 'FYHSite.site.views.games',name='games'),
    url(r'^Movies/(?P<movie_id>\d+)/$', 'FYHSite.site.views.moviedetail'),
    url(r'^Movies/', 'FYHSite.site.views.movie',name='movie'),
    url(r'^Music/', 'FYHSite.site.views.music',name='music'),
    url(r'^Music/(?P<music_id>\d+)/$', 'FYHSite.site.views.musicdetail'),
    url(r'^Used/', 'FYHSite.site.views.used',name='used'),
    url(r'^Used/(?P<used_id>\d+)/$', 'FYHSite.site.views.useddetail'),
    url(r'^cart/', 'FYHSite.site.views.get_cart'),
    url(r'^track/', 'FYHSite.site.views.track',name='track'),
    url(r'^wishlist/', 'FYHSite.site.views.get_wishlist'),
    url(r'^help/', 'FYHSite.site.views.help',name='help'),
    url(r'^stores/', 'FYHSite.site.views.stores',name='stores'),
    url(r'^accounts/deactivate/', 'FYHSite.site.views.deactivate'),
    url(r'^accounts/', 'FYHSite.site.views.account',name='account'),
    #url(r'^accounts/deactivate/', 'FYHSite.site.views.deactivate', name='deactivate'),
    url(r'^account/', include('registration.urls')),
    url(r'^search/', include('haystack.urls')), 
    url(r'^ordertrack/', 'FYHSite.site.views.track',name='track'),
    url(r'^add/','FYHSite.site.views.add_to_cart'),
    url(r'^addlist/','FYHSite.site.views.add_to_wishlist'),
)
