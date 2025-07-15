from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import custom_404, register

# Обработка ошибки 404 / Handling 404 error
handler404 = custom_404

urlpatterns = [
    # Главная страница / Home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # Аутентификация и регистрация / Authentication and registration
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('register/', register, name='register'),
    # Приложения / Applications
    path('menu/', include('menu.urls', namespace='menu')),
    # Админ-панель / Admin panel
    path('control-room/', admin.site.urls),
]

# Обработка статистических файлов в режиме разработки / Processing statistical
# files in development mode
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
