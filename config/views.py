from django.shortcuts import render


def custom_404(request, exception):
    '''Обработка ошибки 404'''
    return render(request, '404.html', status=404)
