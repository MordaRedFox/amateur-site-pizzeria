from django.db import models
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from PIL import Image


# =============================================================================
# Кастомные валидаторы и базовые модели / Custom validators and base models
# =============================================================================
def validate_image_size(image):
    """
    Ограничение размера загружаемого файла до 20 МБ
    Upload file size limit is 20 MB
    """
    limit_mb = 20
    limit = limit_mb * 1024 * 1024
    if image.size > limit:
        raise ValidationError(f'Максимальный размер файла - {limit_mb} MБ')


def validate_image_content(image):
    """
    Проверят, что загружаемый файл действительно является изображением
    Check that the file being uploaded is indeed an image
    """
    try:
        img = Image.open(image)
        img.verify()
        image.seek(0)
    except (IOError, SyntaxError, AttributeError):
        raise ValidationError('Недопустимый формат изображения')


class MenuItem(models.Model):
    """
    Абстрактная базовая модель для элементов меню
    Abstract base model for menu elements
    """
    name = models.CharField(
        'Название блюда',
        max_length=100,
        unique=True,
        help_text='Уникальное название блюда',
    )

    description = models.TextField(
        'Описание блюда',
        blank=True,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0.01)],
        help_text='Цена должна быть положительной',
    )

    weight = models.PositiveBigIntegerField(
        'Вес (г)',
        default=0,
        validators=[MinValueValidator(1)],
        help_text='Вес блюда в граммах',
    )

    image = models.ImageField(
        'Изображение',
        upload_to='menu_images/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size,
            validate_image_content,
        ],
        help_text=('Загрузите изображение блюда (разрешены: .jpg, .jpeg, '
                   '.png; максимальный размер файла - 20 МБ)'),
    )

    calories = models.PositiveBigIntegerField(
        'Калорийность (ккал)',
        default=0,
        validators=[MinValueValidator(1)],
        help_text='Калорийность блюда в килокалориях',
    )

    proteins = models.DecimalField(
        'Белки (г)',
        max_digits=4,
        decimal_places=1,
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Содержание белков в граммах',
    )

    fats = models.DecimalField(
        'Жиры (г)',
        max_digits=4,
        decimal_places=1,
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Содержание жиров в граммах',
    )

    carbohydrates = models.DecimalField(
        'Углеводы (г)',
        max_digits=4,
        decimal_places=1,
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Содержание углеводов в граммах',
    )


    def save(self, *args, **kwargs):
        """
        Автоматическое экранирование HTML перед сохранениием
        Automatically escape HTML before saving
        """
        self.name = strip_tags(self.name)
        self.description = strip_tags(self.description)
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        """
        Удаление модели и связанных с ней файлов изображений
        Deleting a model and its associated image files
        """
        if self.image:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)
        super().delete(*args, **kwargs)


    class Meta:
        abstract = True
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]


    def __str__(self):
        """
        Строковое представление модели
        String representation of the model
        """
        return f'{self.name} - {self.price}₽'


class Topping(models.Model):
    """
    Модель топпингов для блюд
    Model of toppings for dishes
    """
    name = models.CharField(
        'Название',
        max_length=100,
        unique=True,
        help_text='Уникальное название топпинга',
    )

    price_extra = models.DecimalField(
        'Доплата',
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0.01)],
        help_text='Дополнительная стоимость топпинга (неотрицательная)',
    )


    def save(self, *args, **kwargs):
        """
        Автоматическое экранировние HTML перед сохранением
        Automatically escape HTML before saving
        """
        self.name = strip_tags(self.name)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['name']
        verbose_name = 'топпинг'
        verbose_name_plural = 'Топпинги'


    def __str__(self):
        """
        Строковое представление модели
        String representation of the model
        """
        if self.price_extra:
            extra = f' (+{self.price_extra}₽)'
        else:
            extra = ''
        return f'{self.name}{extra}'


class BaseToppingRelation(models.Model):
    """
    Абстрактная модель связи блюда с топпингами
    Abstract model of the relationship between a dish and toppings
    """
    topping = models.ForeignKey(Topping, verbose_name='Топпинг',
                                on_delete=models.CASCADE)


    class Meta:
        abstract = True
        ordering = ['topping__name']


    def __str__(self):
        """
        Строковое представление модели
        String representation of the model
        """
        if hasattr(self, 'item'):
            return f'{self.item.name} + {self.topping.name}'
        return f'Топпинг: {self.topping.name}'


# =============================================================================
# Модели блюд / Models of dishes
# =============================================================================
class Pizza(MenuItem):
    class Meta:
        verbose_name = 'пиццу'
        verbose_name_plural = 'Пиццы'


class Burger(MenuItem):
    class Meta:
        verbose_name = 'бургер'
        verbose_name_plural = 'Бургеры'


class Snack(MenuItem):
    class Meta:
        verbose_name = 'снэк'
        verbose_name_plural = 'Снэки'


class Salad(MenuItem):
    class Meta:
        verbose_name = 'салат'
        verbose_name_plural = 'Салаты'


class Dessert(MenuItem):
    class Meta:
        verbose_name = 'десерт'
        verbose_name_plural = 'Десерты'


class Drink(MenuItem):
    class Meta:
        verbose_name = 'напиток'
        verbose_name_plural = 'Напитки'


# =============================================================================
# Модели связей блюд и топпингов / Models of relationships between dishes
# and toppings
# =============================================================================
class PizzaTopping(BaseToppingRelation):
    item = models.ForeignKey(Pizza, related_name='toppings',
                             verbose_name='Пицца', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('item', 'topping')
        verbose_name = 'топпинг пиццы'
        verbose_name_plural = 'Топпинги пицц'


class BurgerTopping(BaseToppingRelation):
    item = models.ForeignKey(Burger, related_name='toppings',
                             verbose_name='Бургер', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('item', 'topping')
        verbose_name = 'топпинг бургера'
        verbose_name_plural = 'Топпинги бургеров'


class SnackTopping(BaseToppingRelation):
    item = models.ForeignKey(Snack, related_name='toppings',
                             verbose_name='Снэк', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('item', 'topping')
        verbose_name = 'топпинг снэка'
        verbose_name_plural = 'Топпинги снэков'


class SaladTopping(BaseToppingRelation):
    item = models.ForeignKey(Salad, related_name='toppings',
                             verbose_name='Салат', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('item', 'topping')
        verbose_name = 'топпинг салата'
        verbose_name_plural = 'Топпинги салатов'


class DessertTopping(BaseToppingRelation):
    item = models.ForeignKey(Dessert, related_name='toppings',
                             verbose_name='Десерт', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('item', 'topping')
        verbose_name = 'топпинг десерта'
        verbose_name_plural = 'Топпинги десертов'


class DrinkTopping(BaseToppingRelation):
    item = models.ForeignKey(Drink, related_name='toppings',
                             verbose_name='Напиток', on_delete=models.CASCADE)


    class Meta:
        unique_together = ('item', 'topping')
        verbose_name = 'топпинг напитка'
        verbose_name_plural = 'Топпинги напитков'
