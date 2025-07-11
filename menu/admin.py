from django.contrib import admin
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from .models import (Topping, Pizza, Burger, Snack, Salad, Dessert, Drink,
                     PizzaTopping, BurgerTopping, SnackTopping, SaladTopping,
                     DessertTopping, DrinkTopping)


# =============================================================================
# 1. Базовые классы
# =============================================================================

class BaseMenuItemAdmin(admin.ModelAdmin):
    '''Базовый класс админки для меню'''
    list_display = ('name', 'description_short', 'price', 'image_preview')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    list_per_page = 20
    readonly_fields = ('image_preview',)
    fieldsets = [
        ('Основная информация', {
            'fields': ('name', 'description', 'weight', 'price', 'image',
                       'image_preview')
        }),
        ('Энергетическая ценность (на 100 г)', {
            'fields': ('calories', 'proteins', 'fats', 'carbohydrates'),
            'description': 'Укажите данные о энергетической ценности продукта'
        })
    ]

    class Meta:
        ordering = ['name']

    def clean(self):
        '''Проверка на положительную цену и уникальность названия'''
        super().clean()

        # Проверка на положительную цену
        if hasattr(self, 'cleaned_data') and 'price' in self.cleaned_data:
            if self.cleaned_data['price'] <= 0:
                raise ValidationError(
                    {'price': 'Цена должна быть положительной'})

        # Проверка на уникальность назввания
        if hasattr(self, 'cleaned_data') and 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            model = self.model
            # Проверяем, существует ли уже товар с таким именем
            if (model.objects.filter(name=name)
                .exclude(pk=self.instance.pk if self.instance else None)
                .exists()):
                raise ValidationError(
                    {'name': 'Товар с таким названием уже существует'})

    @admin.display(description='Описание')
    def description_short(self, obj):
        '''Сокращает слишком длинные описания блюд в меню'''
        if not obj.description:
            return ''
        return (obj.description[:50] + '...' if len(obj.description) > 50 
                else obj.description)

    @admin.display(description='Превью')
    def image_preview(self, obj):
        '''Превью изображения в админке'''
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return 'Нет изображения'


class ToppingRelationAdmin(admin.ModelAdmin):
    '''Базовый класс для связи топпингов'''
    list_display = ('item_name', 'topping', 'price_with_topping')
    list_filter = ('topping',)
    search_fields = ('topping__name', 'item__name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._verbose_names_cache = {}

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('topping')

    @admin.display(description='Блюдо')
    def item_name(self, obj):
        '''Название блюда без указания типа'''
        return obj.item.name

    @admin.display(description='Итоговая цена')
    def price_with_topping(self, obj):
        '''Общая цена блюда с топпингом'''
        return f'{obj.item.price + obj.topping.price_extra:.2f}₽'


class ToppingInline(admin.TabularInline):
    '''Базовый класс для Inline-топпингов'''
    extra = 1
    verbose_name = 'Топпинг'
    verbose_name_plural = 'Топпинги'
    autocomplete_fields = ['topping']


# =============================================================================
# 2. Inline для топпингов блюд
# =============================================================================

class PizzaToppingInline(ToppingInline):
    model = PizzaTopping


class BurgerToppingInline(ToppingInline):
    model = BurgerTopping


class SnackToppingInline(ToppingInline):
    model = SnackTopping


class SaladToppingInline(ToppingInline):
    model = SaladTopping


class DessertToppingInline(ToppingInline):
    model = DessertTopping


class DrinkToppingInline(ToppingInline):
    model = DrinkTopping


# =============================================================================
# 3. Админки для топпингов и блюд
# =============================================================================

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    '''Админка для топпинга'''
    list_display = ('name', 'price_extra')
    search_fields = ('name',)
    list_filter = ('price_extra',)

    def clean(self):
        '''Проверка на положительную цену и уникальность названия'''
        super().clean()

        # Проверка на положительную цену
        if (hasattr(self, 'cleaned_data') and 'price_extra' in 
            self.cleaned_data):
            if self.cleaned_data['price_extra'] <= 0:
                raise ValidationError(
                    {'price_extra': 'Цена должна быть положительной'})

        # Проверка на уникальность назввания
        if hasattr(self, 'cleaned_data') and 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            model = self.model
            # Проверяем, существует ли уже товар с таким именем
            if (model.objects.filter(name=name)
                .exclude(pk=self.instance.pk if self.instance else None)
                .exists()):
                raise ValidationError(
                    {'name': 'Топпинг с таким названием уже существует'})


@admin.register(Pizza)
class PizzaAdmin(BaseMenuItemAdmin):
    inlines = [PizzaToppingInline]


@admin.register(Burger)
class BurgerAdmin(BaseMenuItemAdmin):
    inlines = [BurgerToppingInline]


@admin.register(Snack)
class SnackAdmin(BaseMenuItemAdmin):
    inlines = [SnackToppingInline]


@admin.register(Salad)
class SaladAdmin(BaseMenuItemAdmin):
    inlines = [SaladToppingInline]


@admin.register(Dessert)
class DessertAdmin(BaseMenuItemAdmin):
    inlines = [DessertToppingInline]


@admin.register(Drink)
class DrinkAdmin(BaseMenuItemAdmin):
    inlines = [DrinkToppingInline]


# =============================================================================
# 4. Админки для топпингов и блюд
# =============================================================================

@admin.register(PizzaTopping)
class PizzaToppingAdmin(ToppingRelationAdmin):
    pass


@admin.register(BurgerTopping)
class BurgerToppingAdmin(ToppingRelationAdmin):
    pass


@admin.register(SnackTopping)
class SnackToppingAdmin(ToppingRelationAdmin):
    pass


@admin.register(SaladTopping)
class SaladToppingAdmin(ToppingRelationAdmin):
    pass


@admin.register(DessertTopping)
class DessertToppingAdmin(ToppingRelationAdmin):
    pass


@admin.register(DrinkTopping)
class DrinkToppingAdmin(ToppingRelationAdmin):
    pass
