from django.urls import path
from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.menu_categories, name='categories'),
    path('<str:category>/', views.menu_items, name='items'),
    path('<str:category>/<int:pk>/', views.menu_item_detail, 
         name='item_detail'),
]
