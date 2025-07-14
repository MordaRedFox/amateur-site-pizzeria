from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def custom_404(request, exception):
    '''Обработка ошибки 404'''
    return render(request, '404.html', status=404)

def register(request):
    '''Обработка входа или регистрации пользователя'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'{username}, ваш аккаунт создан! Теперь вы можете войти'
            )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
