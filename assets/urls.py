from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AssetList, AssetDetail


urlpatterns = [
    url(r'^$', AssetList.as_view(), name='asset-list'),
    url(r'^(?P<pk>[0-9]+)/$', AssetDetail.as_view(), name='asset-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
