from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView
from users.views import CustomLoginView, register
from .views import custom_404


handler404 = custom_404

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),
    path('register/', register, name='register'),
    path('menu/', include('menu.urls', namespace='menu')),
    path('users/', include('users.urls', namespace='users')),
    path('control-room/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
