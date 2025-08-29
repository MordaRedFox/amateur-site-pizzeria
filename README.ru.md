<div align="center">

# 🍕 Amateur Site Pizzeria 🍕

## Сменить язык: [English](README.md)

[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

---

## ⚠️ Юридическое уведомление
**Данный проект разработан исключительно в образовательных целях** для изучения фреймворка Django и веб-разработки.

Сайт представляет собой фанатский проект, вдохновленный вселенной Five Nights at Freddy's, со следующими ограничениями:
- 🚫 Не используются материалы, защищенные авторским правом
- 🚫 Не применяется оригинальный контент из игр серии
- 🚫 Не является коммерческим или официальным продуктом
- 🚫 Соблюдены принципы добросовестного использования

Проект включает только исходный код, медиафайлы не распространяются.

---

## 🌟 Ключевые возможности

<div align="center">

<table>
    <tr>
        <td valign="top" width="50%">
            <h3 align="center">👨‍🍳 Функционал пиццерии</h3>
            <p align="center">
                <img src="https://img.shields.io/badge/🍕-Интерактивное%20меню-orange"
                    alt="Интерактивное меню">
                <img src="https://img.shields.io/badge/📋-Категоризация%20товаров-green"
                    alt="Категоризация товаров">
                <img src="https://img.shields.io/badge/🖼️-Управление%20медиа-blue"
                    alt="Управление медиа">
            </p>
            <div style="text-align: left; margin-left: 20px;">
                <ul style="text-align: left; padding-left: 20px;">
                    <li>🍕 Полнофункциональное меню с системой категорий</li>
                    <li>📋 Детализированная информация о продукции с характеристиками</li>
                    <li>🖼️ Динамическая загрузка изображений через административный интерфейс</li>
                    <li>🔍 Интуитивная навигация и система поиска по категориям</li>
                </ul>
            </div>
        </td>
        <td valign="top" width="50%">
            <h3 align="center">👤 Система пользователей</h3>
            <p align="center">
                <img src="https://img.shields.io/badge/🔐-Система%20аутентификация-purple"
                    alt="Аутентификация">
                <img src="https://img.shields.io/badge/👨‍💻-Управление%20профилями-blue"
                    alt="Управление профилями">
                <img src="https://img.shields.io/badge/🛡️-Продвинутая%20безопасность-red"
                    alt="Продвинутая безопасность">
            </p>
            <div style="text-align: left; margin-left: 20px;">
                <ul style="text-align: left; padding-left: 20px;">
                    <li>🔐 Полноценная система регистрации и аутентификации</li>
                    <li>👨‍💻 Персонализированные пользовательские профили</li>
                    <li>🛡️ Защита от brute-force атак с использованием django-axes</li>
                    <li>🔒 Автоматическая блокировка при обнаружении подозрительной активности</li>
                </ul>
            </div>
        </td>
    </tr>
</table>

</div>

> **📱 Адаптивный дизайн**: Сайт безупречно отображается на всех устройствах — от десктопов до смартфонов. Интерактивные элементы украшены плавными анимациями при наведении и фокусе.

---

## 🛠 Технологический стек

<div align="center">

<table>
    <tr>
        <th>Компонент</th>
        <th>Версия</th>
        <th>Назначение</th>
        <th>Бейдж</th>
    </tr>
    <tr align="center">
        <td>Python</td>
        <td>3.11+</td>
        <td>Основной язык программирования</td>
        <td><img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python"></td>
    </tr>
    <tr align="center">
        <td>JavaScript</td>
        <td>ES6+</td>
        <td>Интерактивность и скрипты</td>
        <td><img src="https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript"></td>
    </tr>
    <tr align="center">
        <td>CSS</td>
        <td>3</td>
        <td>Стилизация и оформление</td>
        <td><img src="https://img.shields.io/badge/CSS-3-1572B6?logo=css3&logoColor=white" alt="CSS"></td>
    </tr>
    <tr align="center">
        <td>HTML</td>
        <td>5</td>
        <td>Разметка и структура страниц</td>
        <td><img src="https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white" alt="HTML"></td>
    </tr>
    <tr align="center">
        <td>Django</td>
        <td>5.2</td>
        <td>Бэкенд-фреймворк</td>
        <td><img src="https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white" alt="Django"></td>
    </tr>
    <tr align="center">
        <td>SQLite3</td>
        <td>-</td>
        <td>База данных по умолчанию</td>
        <td><img src="https://img.shields.io/badge/SQLite3-3.42%2B-003B57?logo=sqlite&logoColor=white" alt="SQLite3"></td>
    </tr>
    <tr align="center">
        <td>Pillow</td>
        <td>11.2.1</td>
        <td>Обработка изображений</td>
        <td><img src="https://img.shields.io/badge/Pillow-11.2.1-8A2BE2?logo=python&logoColor=white" alt="Pillow"></td>
    </tr>
    <tr align="center">
        <td>django-axes</td>
        <td>8.0.0</td>
        <td>Защита от brute-force атак</td>
        <td><img src="https://img.shields.io/badge/django--axes-8.0.0-FF6B6B?logo=shield&logoColor=white" alt="django-axes"></td>
    </tr>
    <tr align="center">
        <td>django-cleanup</td>
        <td>9.0.0</td>
        <td>Управление медиафайлами</td>
        <td><img src="https://img.shields.io/badge/django--cleanup-9.0.0-00BFFF?logo=clean&logoColor=white" alt="django-cleanup"></td>
    </tr>
    <tr align="center">
        <td>django-csp</td>
        <td>4.0</td>
        <td>Политика безопасности</td>
        <td><img src="https://img.shields.io/badge/django--csp-4.0-228B22?logo=security&logoColor=white" alt="django-csp"></td>
    </tr>
    <tr align="center">
        <td>python-dotenv</td>
        <td>1.1.0</td>
        <td>Управление конфигурацией</td>
        <td><img src="https://img.shields.io/badge/python--dotenv-1.1.0-FFD700?logo=python&logoColor=white" alt="python-dotenv"></td>
    </tr>
</table>

</div>

---

## 📦 Установка и развертывание

### 📋 Системные требования
- Python 3.10 или новее
- Рекомендуется использование виртуального окружения

### 🔧 Конфигурация
1. Клонируйте репозиторий проекта
2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# или
.venv\Scripts\activate  # Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Настройте переменные окружения в файле .env:
```python
SECRET_KEY = 'your-secret-key-here' # Замените на ваш секретный ключ
DEBUG = True
```
5. Примените миграции (автоматически создается база данных):
```bash
python manage.py migrate
```
6. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
7. Запустите сервер (локально на своём ПК):
```bash
python manage.py runserver
```

---

## 🌿 СТРАТЕГИЯ ВЕТВЛЕНИЯ
Проект использует систему управления версиями с двумя основными ветками:

### 🛠️ Ветка development
**Назначение**: Активная разработка новых функций

**Особенности**:
- Полные исходные файлы с комментариями
- Несжатые CSS и JavaScript файлы
- Экспериментальные возможности
- Детальная документация в коде

### 🚀 Ветка main
**Назначение**: Стабильные production-сборки

**Особенности**:
- Оптимизированные и сжатые CSS и JavaScript файлы
- Очищенный от комментариев код
- Готовые к развертыванию версии

---

## 📁 Структура проекта (main)
```
amateur-site-pizzeria/
├── .venv/                       # Виртуальное окружение Python (не добавляется в git)
├── config/                      # Основной пакет конфигурации проекта
│   ├── __init__.py              # Помечает директорию как Python-пакет
│   ├── asgi.py                  # Конфигурация ASGI для асинхронных серверов
│   ├── settings.py              # Основные настройки проекта (БД, приложения, middleware)
│   ├── urls.py                  # Главный файл маршрутизации URL всего проекта
│   ├── views.py                 # Глобальные view-функции проекта
│   └── wsgi.py                  # Конфигурация WSGI для развертывания на сервере
├── media/                       # Директория для загружаемых админом изображений блюд
│   └── menu_images/
├── menu/                        # Приложение для управления меню пиццерии
│   ├── migrations/              # Миграции базы данных для моделей меню
│   ├── __init__.py              # Помечает директорию как Python-пакет
│   ├── admin.py                 # Регистрация моделей в админ-панели Django
│   ├── apps.py                  # Конфигурация приложения menu
│   ├── models.py                # Модели данных
│   ├── urls.py                  # Маршрутизация URL для приложения menu
│   └── views.py                 # View-функции для работы с меню
├── readme_images/               # Картинки для README файла
├── static/                      # Статические файлы (CSS, JS, изображения, шрифты)
│   ├── css/                     # Стили CSS для различных страниц
│   │   ├── 404.css              # Стили для страницы 404 ошибки
│   │   ├── base.css             # Базовые стили (общие для всех страниц)
│   │   ├── home.css             # Стили для главной страницы
│   │   ├── locked.css           # Стили для страницы блокировки аккаунта
│   │   ├── menu.css             # Стили для страниц меню
│   │   ├── profile.css          # Стили для страницы профиля
│   │   └── registration.css     # Стили для страниц регистрации и авторизации
│   ├── font_awesome/            # Библиотека иконок Font Awesome
│   ├── js/                      # JavaScript файлы
│   │   ├── 404.js               # JS для страницы 404 ошибки
│   │   ├── home.js              # JS для главной страницы
│   │   ├── locked.js            # JS для страницы блокировки
│   │   └── password_toggle.js   # Переключение видимости пароля
│   ├── media/                   # Статические медиафайлы
│   │   ├── error_404/           # Медиафайлы для страницы 404
│   │   │   ├── ring.mp3
│   │   │   ├── static.mp3
│   │   │   └── whisper.mp3
│   │   ├── favicon/             # Фавиконки сайта
│   │   ├── home/                # Медиафайлы для главной страницы
│   │   │   ├── home1.png
│   │   │   ├── home2.png
│   │   │   ├── home3.png
│   │   │   ├── home4.png
│   │   │   ├── click.mp3
│   │   │   ├── secret.mp3
│   │   │   ├── scream.mp3
│   │   │   └── screamer.mp4
│   │   └── menu/                # Медиафайлы для меню
│   │       └── image_missing.png
├── templates/                   # HTML шаблоны
│   ├── menu/
│   │   ├── categories.html      # Шаблон категорий меню
│   │   ├── item_detail.html     # Шаблон конкретного блюда
│   │   └── items.html           # Шаблон блюд конкретной категории
│   ├── registration/
│   │   ├── logged_out.html      # Шаблон выхода из аккаунта
│   │   ├── login.html           # Шаблон входа в аккаунт
│   │   └── register.html        # Шаблон регистрации
│   ├── users/
│   │   ├── locked.html          # Шаблон блокировки пользователя
│   │   └── profile.html         # Шаблон личного профиля пользователя
│   ├── 404.html                 # Шаблон 404 ошибки
│   ├── base.html                # Базовый шаблон
│   └── home.html                # Шаблон главной страницы
├── users/                       # Приложение для управления пользователями
│   ├── __init__.py              # Помечает директорию как Python-пакет
│   ├── apps.py                  # Конфигурация приложения users
│   ├── forms.py                 # Формы для регистрации и авторизации
│   ├── urls.py                  # Маршрутизация URL для приложения users
│   └── views.py                 # View-функции для работы с пользователями
├── .env                         # Файл с переменными окружения (секреты, настройки)
├── .gitignore                   # Файлы и директории, игнорируемые git
├── db.sqlite3                   # База данных SQLite (не добавляется в git)
├── LICENSE                      # Лицензия проекта
├── README.md                    # Документация проекта на английском
├── README.ru.md                 # Документация проекта на русском
├── requirements.txt             # Зависимости Python проекта
└── manage.py                    # Основной скрипт для управления проектом Django
```

---

## 📸 Предварительный просмотр
> ⚠️ **Примечание**: Сайт временно не размещен на хостинге. Для ознакомления прилагаю скриншоты основных страниц. Изображения заблюрены из-за авторских прав.

### 🏠 Главная страница
![Главная страница](readme_images/1.png)
![Главная страница](readme_images/2.png)
![Главная страница](readme_images/3.png)
> **Примечание**: На главной странице присутствует интерактив с терминалом.

### 🍔 Меню
![Меню](readme_images/4.png)
![Меню](readme_images/5.png)
![Меню](readme_images/6.png)
> **Примечание**: Меню загружается из базы данных сайта.

### 🔐 Вход и регистрация
![Вход и регистрация](readme_images/7.png)
![Вход и регистрация](readme_images/8.png)
> **Примечание**: Есть скрипт для просмотра и скрытия вводимого пароля.

### 👤 Личный кабинет
![Личный кабинет](readme_images/9.png)
![Личный кабинет](readme_images/10.png)
> **Примечание**: Можно редактировать часть данных.

### ⚙️ Административный сайт
![Административный сайт](readme_images/11.png)
![Административный сайт](readme_images/12.png)
> **Примечание**: Изменение блюд меню и добавление новых с загрузкой изображений.

---

## 🎯 Образовательные цели
Проект реализован для освоения ключевых аспектов веб-разработки:
- ✅ Архитектура MVC/MVT - Понимание структуры Django-приложений
- ✅ ORM и миграции - Работа с моделями данных и миграциями
- ✅ Аутентификация - Реализация систем безопасности пользователей
- ✅ Статика и медиа - Управление статическими и динамическими ресурсами
- ✅ Административный интерфейс - Создание панелей управления
- ✅ Безопасность веб-приложений - Защита от распространенных уязвимостей
- ✅ Оптимизация производительности - Методы улучшения скорости работы

## ⚠️ Важное примечание
Этот проект был разработан начинающим программистом-самоучкой. Код может содержать:
- ❌ Ошибки и баги
- ⚡ Неоптимальные решения
- 🛡️ Недочёты в архитектуре

---

## 📩 Контакты
Я открыт для конструктивной критики и предложений по улучшению кода. Если вы нашли ошибку или знаете, как сделать что-то лучше - пожалуйста, свяжитесь со мной!

[![Telegram](https://img.shields.io/badge/-MordaRedFox-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/MordaRedFox)
&nbsp;
[![Email](https://img.shields.io/badge/-mordaredfox@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mordaredfox@gmail.com)
