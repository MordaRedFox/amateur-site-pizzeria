from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def custom_404(request, exception):
    """
    Обработка ошибки 404
    Handling 404 error
    """
    return render(request, '404.html', status=404)


def register(request):
    """
    Обработка входа или регистрации пользователя
    Processing user login or registration
    """
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
