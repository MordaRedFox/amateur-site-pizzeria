from django.shortcuts import render, get_object_or_404
from .models import (Pizza, Burger, Snack, Salad, Dessert, Drink,
                     PizzaTopping, BurgerTopping, SnackTopping, SaladTopping,
                     DessertTopping, DrinkTopping)


MODEL_MAP = {
    'pizza': Pizza,
    'burger': Burger,
    'snack': Snack,
    'salad': Salad,
    'dessert': Dessert,
    'drink': Drink,
}

TOPPING_MAP = {
    Pizza: PizzaTopping,
    Burger: BurgerTopping,
    Snack: SnackTopping,
    Salad: SaladTopping,
    Dessert: DessertTopping,
    Drink: DrinkTopping,
}


def menu_categories(request):
    """
    Представление страницы категорий меню
    View of the menu categories page
    """
    categories = [
        {'name': 'Пицца', 'url': 'pizza', 'count': Pizza.objects.count(),
         'icon': '🍕'},
        {'name': 'Бургеры', 'url': 'burger', 'count': Burger.objects.count(),
         'icon': '🍔'},
        {'name': 'Снэки', 'url': 'snack', 'count': Snack.objects.count(),
         'icon': '🍟'},
        {'name': 'Салаты', 'url': 'salad', 'count': Salad.objects.count(),
         'icon': '🥗'},
        {'name': 'Десерты', 'url': 'dessert', 'count': Dessert.objects.count(),
         'icon': '🍰'},
        {'name': 'Напитки', 'url': 'drink', 'count': Drink.objects.count(),
         'icon': '🥤'},
    ]

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
    model = MODEL_MAP.get(category)
    if not model:
        return render(request, '404.html', status=404)

    items = model.objects.all()
    category_name = model._meta.verbose_name_plural.capitalize()

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
    model = MODEL_MAP.get(category)
    if not model:
        return render(request, '404.html', status=404)

    item = get_object_or_404(model, pk=pk)
    topping_model = TOPPING_MAP.get(model)
    toppings = topping_model.objects.filter(item=item).select_related(
        'topping')

    context = {
        'item': item,
        'toppings': toppings,
        'category': category,
        'title': f'{item.name} | Animatronic Pizzeria',
    }
    return render(request, 'menu/item_detail.html', context)
