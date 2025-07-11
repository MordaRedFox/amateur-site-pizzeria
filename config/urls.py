'''Главный URL-диспетчер'''
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import custom_404

# Обработка ошибки 404
handler404 = custom_404

urlpatterns = [
    path('control-room/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('menu/', include('menu.urls', namespace='menu')),
]

# Обработка статистических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
