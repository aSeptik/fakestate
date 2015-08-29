from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
	#url(r'^items/', views.ItemsList.as_view()),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^fakestate/', include('fakestate.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
