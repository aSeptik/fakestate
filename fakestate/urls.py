from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
	url(r'^items/$', views.ItemsList),
	url(r'^items/(?P<pk>[0-9]+)$', views.SingleItem),
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)