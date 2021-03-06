"""ModelServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'MR Interior Design Server API'
API_DESCRIPTION = 'A Web API for creating and viewing cloud database.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION,
                                     authentication_classes=[], permission_classes=[],
                                     ),
        ),
    url(r'^category/', include('categories.urls')),
    url(r'^asset/', include('assets.urls')),
    url(r'^descriptor/', include('descriptors.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
