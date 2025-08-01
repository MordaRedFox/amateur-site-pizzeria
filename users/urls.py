from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('locked/', views.locked_out_view, name='locked'),
]
