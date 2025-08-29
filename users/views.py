import time
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from axes.models import AccessAttempt
from .forms import CustomUserCreationForm, ProfileEditForm


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Профиль успешно обновлен!')
                return redirect('users:profile')
            
            except Exception as e:
                messages.error(
                    request,
                    'Произошла непредвиденная ошибка при обновлении профиля!'
                )
    else:
        form = ProfileEditForm(instance=request.user)
    
    context = {
        'user': request.user,
        'form': form,
        'edit_mode': 'edit' in request.GET
    }
    return render(request, 'users/profile.html', context)


def locked_out_view(request):
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
            unlock_time = attempt.attempt_time + timezone.timedelta(
                hours=settings.AXES_COOLOFF_TIME)
            unlock_timestamp = int(unlock_time.timestamp())
    except Exception:
        unlock_timestamp = int(time.time()) + default_unlock_period

    context = {'unlock_timestamp': unlock_timestamp}
    return render(request, 'users/locked.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'{username}, ваш аккаунт создан! Теперь вы можете войти'
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


    def form_invalid(self, form):
        response = super().form_invalid(form)
        ip = self.request.META.get('REMOTE_ADDR', '')
        user_agent = self.request.META.get('HTTP_USER_AGENT', '')

        attempt = AccessAttempt.objects.filter(
            ip_address=ip,
            user_agent=user_agent
        ).order_by('-attempt_time').first()

        if attempt:
            remaining_attempts = max(
                0, settings.AXES_FAILURE_LIMIT - attempt.failures_since_start)
        else:
            remaining_attempts = settings.AXES_FAILURE_LIMIT

        response.context_data['remaining_attempts'] = remaining_attempts
        return response


    def dispatch(self, request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        attempt = AccessAttempt.objects.filter(
            ip_address=ip,
            user_agent=user_agent
        ).order_by('-attempt_time').first()

        if (attempt and
                attempt.failures_since_start >= settings.AXES_FAILURE_LIMIT):
            if self.is_user_locked(attempt):
                return HttpResponseRedirect(reverse('users:locked'))

        return super().dispatch(request, *args, **kwargs)


    def is_user_locked(self, attempt):
        cooloff_time = attempt.attempt_time + timezone.timedelta(
            hours=settings.AXES_COOLOFF_TIME)
        return cooloff_time > timezone.now()
