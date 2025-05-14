from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from personal.views import (
    home_screen_view,
    speakers_view,
    register,
    success,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('speakers/', speakers_view, name='speakers'),
    path('registration/', register, name='register'),
    path('success/', success, name="success")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)