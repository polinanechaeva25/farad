from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

admin.autodiscover()


urlpatterns = [
    path('', include('mainapp.urls', namespace='mainapp')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))