from django.shortcuts import render, get_object_or_404
from .models import (Pizza, Burger, Snack, Salad, Dessert, Drink,
                     PizzaTopping, BurgerTopping, SnackTopping, SaladTopping,
                     DessertTopping, DrinkTopping)


CATEGORY_CONFIG = {
    'pizza': {'model': Pizza, 'name': 'Пицца', 'icon': '🍕',
                'topping_model': PizzaTopping},
    'burger': {'model': Burger, 'name': 'Бургеры', 'icon': '🍔',
                'topping_model': BurgerTopping},
    'snack': {'model': Snack, 'name': 'Снэки', 'icon': '🍟',
                'topping_model': SnackTopping},
    'salad': {'model': Salad, 'name': 'Салаты', 'icon': '🥗',
                'topping_model': SaladTopping},
    'dessert': {'model': Dessert, 'name': 'Десерты', 'icon': '🍰',
                'topping_model': DessertTopping},
    'drink': {'model': Drink, 'name': 'Напитки', 'icon': '🥤',
                'topping_model': DrinkTopping},
}


def menu_categories(request):
    """
    Представление страницы категорий меню
    View of the menu categories page
    """
    categories = []
    for url, config in CATEGORY_CONFIG.items():
        categories.append({
            'name': config['name'],
            'url': url,
            'count': config['model'].objects.count(),
            'icon': config['icon']
        })

    context = {
        'categories': categories,
        'title': 'Меню Animatronic Pizzeria',      
    }
    return render(request, 'menu/categories.html', context)


def menu_items(request, category):
    """
    Представление страницы списка блюд в категории
    View of the list page of dishes in a category
    """
    config = CATEGORY_CONFIG.get(category)
    if not config:
        return render(request, '404.html', status=404)

    items = config['model'].objects.all()
    category_name = config['name']

    context = {
        'items': items,
        'category': category,
        'category_name': category_name,
        'title': f'{category_name} | Animatronic Pizzeria',
    }
    return render(request, 'menu/items.html', context)


def menu_item_detail(request, category, pk):
    """
    Представление страницы со всей информацией о блюде
    View of a page with all the information about the dish
    """
    config = CATEGORY_CONFIG.get(category)
    if not config:
        return render(request, '404.html', status=404)

    item = get_object_or_404(config['model'], pk=pk)
    if config['topping_model']:
        topping_model = config['topping_model']
        toppings = topping_model.objects.filter(item=item).select_related(
            'topping')
    else:
        toppings = []

    context = {
        'item': item,
        'toppings': toppings,
        'category': category,
        'title': f'{item.name} | Animatronic Pizzeria',
    }
    return render(request, 'menu/item_detail.html', context)
