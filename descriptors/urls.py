from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DescriptorList, DescriptorDetail


urlpatterns = [
    url(r'^$', DescriptorList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DescriptorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
