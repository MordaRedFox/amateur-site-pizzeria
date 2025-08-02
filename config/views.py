from django.shortcuts import render


def custom_404(request, exception):
    """
    Обработка ошибки 404
    Handling 404 error
    """
    return render(request, '404.html', status=404)
