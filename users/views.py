from django.shortcuts import render
from axes.models import AccessAttempt
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import time


def locked_out_view(request):
    """
    Обработчик страницы блокировки, вычисляет время разблокировки и передаёт
    его в шаблон
    The lock page handler calculates the unlock time and passes it to the
    template
    """
    ip = request.META.get('REMOTE_ADDR', '')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    default_unlock_period = settings.AXES_COOLOFF_TIME * 3600
    unlock_timestamp = int(time.time()) + default_unlock_period

    try:
        attempt = AccessAttempt.objects.filter(
            ip_address=ip,
            user_agent=user_agent,
            failures_since_start__gte=1
        ).order_by('-attempt_time').first()

        if attempt:
            # Вычисляем время разблокировки / Calculating the unlock time
            unlock_time = attempt.attempt_time + timezone.timedelta(
                hours=settings.AXES_COOLOFF_TIME)
            unlock_timestamp = int(unlock_time.timestamp())
    except Exception:
        # В случае ошибки используем время по умолчанию / In case of error,
        # use the default time
        unlock_timestamp = int(time.time()) + default_unlock_period

    context = {'unlock_timestamp': unlock_timestamp}
    return render(request, 'users/locked.html', context)


class CustomLoginView(LoginView):
    """
    Кастомный класс для обработки входа с проверкой блокировки
    Custom class for handling login with blocking check
    """
    template_name = 'registration/login.html'


    def form_invalid(self, form):
        """
        Счётчик оставшихся попыток входа в аккаунт до блокировки
        Counter of remaining attempts to log into the account before blocking
        """
        response = super().form_invalid(form)
        ip = self.request.META.get('REMOTE_ADDR', '')
        user_agent = self.request.META.get('HTTP_USER_AGENT', '')

        # Получаем последнюю попытку входа для этого IP/User-Agent / Get the
        # last login attempt for this IP/User-Agent
        attempt = AccessAttempt.objects.filter(
            ip_address=ip,
            user_agent=user_agent
        ).order_by('-attempt_time').first()

        # Вычисляем оставшиеся попытки / Calculate the remaining attempts
        if attempt:
            remaining_attempts = max(
                0, settings.AXES_FAILURE_LIMIT - attempt.failures_since_start)
        else:
            remaining_attempts = settings.AXES_FAILURE_LIMIT

        response.context_data['remaining_attempts'] = remaining_attempts
        return response


    def dispatch(self, request, *args, **kwargs):
        """
        Переопределённый метод dispatch - первая точка входа для запроса.
        Проверяет, не заблокирован ли пользователь
        The overridden dispatch method is the first entry point for a request.
        Checks if the user is blocked
        """
        ip = request.META.get('REMOTE_ADDR', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        attempt = AccessAttempt.objects.filter(
            ip_address=ip,
            user_agent=user_agent
        ).order_by('-attempt_time').first()

        # Проверяем условия блокировки / Checking the blocking conditions
        if (attempt and
                attempt.failures_since_start >= settings.AXES_FAILURE_LIMIT):
            if self.is_user_locked(attempt):
                return HttpResponseRedirect(reverse('users:locked'))

        # Если пользователь не заблокирован - стандартная обработка / If the
        # user is not blocked - standard processing
        return super().dispatch(request, *args, **kwargs)


    def is_user_locked(self, attempt):
        """
        Проверяет, действует ли ещё блокировка для данной попытки
        Checks if the lock is still in effect for the given attempt
        """
        cooloff_time = attempt.attempt_time + timezone.timedelta(
            hours=settings.AXES_COOLOFF_TIME)
        return cooloff_time > timezone.now()
