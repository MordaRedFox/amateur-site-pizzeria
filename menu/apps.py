from django.apps import AppConfig


class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
    verbose_name = ('Меню ресторана')

    @staticmethod
    def validate_menu_item(sender, instance, **kwargs):
        """
        Дополнительная валидация элементов меню перед сохранением
        Additional validation of menu items before saving
        """
        if instance.price <= 0:
            raise ValueError('Цена должна быть положительной')
