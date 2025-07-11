import os
from pathlib import Path
from dotenv import load_dotenv


# =============================================================================
# 1. Базовые настройки и переменные окружения
# =============================================================================

# Загрузка переменных окружения из файла .env
load_dotenv()

# Базовый путь к директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# 2. Основные настройки Django
# =============================================================================

# СЕКРЕТНЫЙ КЛЮЧ: храните это значение в тайне в продакшене!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# РЕЖИМ ОТЛАДКИ: в продакшене должно быть False
DEBUG = True

# Список разрешенных хостов/доменов
ALLOWED_HOSTS = ['*'] if DEBUG else []

# Главный URL-конфиг проекта
ROOT_URLCONF = 'config.urls'

# WSGI-приложение для развертывания
WSGI_APPLICATION = 'config.wsgi.application'

# Тип поля по умолчанию для первичных ключей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =============================================================================
# 3. Приложения, middleware и настройка шаблонов
# =============================================================================

INSTALLED_APPS = [
    # Стандартные приложения Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние приложения
    'axes',
    'django_cleanup.apps.CleanupConfig',
    'csp',

    # Локальные приложения проекта
    'menu',
]

MIDDLEWARE = [
    # Middleware для безопасности
    'django.middleware.security.SecurityMiddleware',

    # Стандартные middleware Django
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Сторонние middleware
    'axes.middleware.AxesMiddleware',
    'csp.middleware.CSPMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =============================================================================
# 4. Настройки базы данных
# =============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================================================================
# 5. Интернационализация и локализация
# =============================================================================

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True


# =============================================================================
# 6. Статические и медиа файлы
# =============================================================================

# Статические файлы (CSS, JS, изображения)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Настройки медиа файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =============================================================================
# 7. Аутентификация, авторизация и безопасность сессий
# =============================================================================

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'UserAttributeSimilarityValidator'),
        'OPTIONS': {
            'user_attributes': ('username', 'email', 'first_name',
                                'last_name'),
            'max_similarity': 0.7,
        }
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'MinimumLengthValidator'),
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'NumericPasswordValidator'),
    },
]

# Настройки сессии
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = '__secure-session-id' if not DEBUG else 'sessionid'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_SECURE = not DEBUG
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Настройки CSRF
CSRF_COOKIE_NAME = '__secure-csrf-token' if not DEBUG else 'csrftoken'
CSRF_COOKIE_SECURE = not DEBUG
CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'

# Бэкенды аутентификации
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Настройки защиты от брутфорса
AXES_ENABLED = not DEBUG
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = 'users/locked.html'
AXES_LOCKOUT_URL = '/users/locked'
AXES_LOCKOUT_PARAMETERS = [["ip_address", "user_agent"]]
AXES_RESET_ON_SUCCESS = True


# =============================================================================
# 8. Настройки CSP (Content Security Policy)
# =============================================================================

CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ["'self'"],
        'script-src': [
            "'self'",
            "'unsafe-inline'",
            "https://cdn.jsdelivr.net",
            "'unsafe-eval'" if DEBUG else None,
        ],
        'style-src': [
            "'self'",
            "'unsafe-inline'",
            "https://cdn.jsdelivr.net",
        ],
        'img-src': ["'self'", "data:"],
        'font-src': ["'self'"],
        'connect-src': (["'self'", "ws://localhost:8000"] if DEBUG 
                        else ["'self'"]),
        'frame-ancestors': ["'none'"],
        'form-action': ["'self'"],
        'base-uri': ["'self'"],
    }
}


# =============================================================================
# 9. Production настройки
# =============================================================================

if not DEBUG:
    # Настройки HTTPS
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Настройки HSTS (HTTP Strict Transport Security)
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Политика Referrer
    SECURE_REFERRER_POLICY = 'same-origin'

    # Защита от кликджекинга
    SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'

    # Оптимизация CSP
    CONTENT_SECURITY_POLICY['DIRECTIVES'].update({
        'script-src': ["'self'", "https://cdn.jsdelivr.net"],
        'style-src': ["'self'", "https://cdn.jsdelivr.net"],
        'worker-src': ["'self'"],
    })
