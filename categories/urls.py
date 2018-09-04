from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryListView, SubCategoryListView, CategoryDetailView, SubCategoryDetailView


urlpatterns = [
    url(r'^$', CategoryListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', CategoryDetailView.as_view()),
    url(r'^sub/$', SubCategoryListView.as_view()),
    url(r'^sub/(?P<pk>[0-9]+)/$', SubCategoryDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
