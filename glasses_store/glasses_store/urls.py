from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from glasses_store.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('users/', include('users.urls')),
    path('glasses/', include('glasses.urls')),
    path('recommendation/', include('recommendation.urls')),
    path('tryon/', include('tryon.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)