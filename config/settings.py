import os
from pathlib import Path
from dotenv import load_dotenv


# =============================================================================
# 1. Базовые настройки и переменные окружения
# 1. Basic settings and environment variables
# =============================================================================

# Загрузка переменных окружения из файла .env / # Load environment variables
# from .env file
load_dotenv()

# Базовый путь к директории проекта / Base path to the project directory
BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# 2. Основные настройки Django
# 2. Basic Django settings
# =============================================================================

# СЕКРЕТНЫЙ КЛЮЧ: храните это значение в тайне в продакшене! / SECRET KEY:
# keep this value secret in production!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# РЕЖИМ ОТЛАДКИ: в продакшене должно быть False / DEBUG MODE: should be
# False in production
DEBUG = True

# Список разрешенных хостов / List of allowed hosts
ALLOWED_HOSTS = ['*'] if DEBUG else []

# Главный URL-конфиг проекта / Main URL config of the project
ROOT_URLCONF = 'config.urls'

# WSGI-приложение для развертывания / WSGI application for deployment
WSGI_APPLICATION = 'config.wsgi.application'

# Тип поля по умолчанию для первичных ключей / Default field type for
# primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =============================================================================
# 3. Приложения, middleware и настройка шаблонов
# 3. Applications, middleware and template customization
# =============================================================================

INSTALLED_APPS = [
    # Стандартные приложения Django / Standard Django applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние приложения / Third party applications
    'axes',
    'django_cleanup.apps.CleanupConfig',
    'csp',

    # Локальные приложения проекта / Local project applications
    'menu',
    'users',
]

MIDDLEWARE = [
    # Middleware для безопасности / Middleware for security
    'django.middleware.security.SecurityMiddleware',

    # Стандартные middleware Django / Standard Django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Сторонние middleware / Third-party middleware
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
# 4. Database settings
# =============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================================================================
# 5. Интернационализация и локализация
# 5. Internationalization and localization
# =============================================================================

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True


# =============================================================================
# 6. Статические и медиа файлы
# 6. Static and media files
# =============================================================================

# Статические файлы (CSS, JS, изображения) / Static files (CSS, JS, images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Настройки медиа файлов / Media file settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =============================================================================
# 7. Аутентификация, авторизация и безопасность сессий
# 7. Authentication, authorization and session security
# =============================================================================

# Перенаправление после входа в аккаунт / Redirect after logging into
# your account
LOGIN_REDIRECT_URL = 'home'

# Валидация паролей / Password validation
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

# Настройки сессии / Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = '__secure-session-id' if not DEBUG else 'sessionid'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_SECURE = not DEBUG
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Настройки CSRF / CSRF settings
CSRF_COOKIE_NAME = '__secure-csrf-token' if not DEBUG else 'csrftoken'
CSRF_COOKIE_SECURE = not DEBUG
CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'

# Бэкенды аутентификации / Authentication backends
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Настройки защиты от брутфорса / Brute force protection settings
AXES_ENABLED = not DEBUG
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = 'users/locked.html'
AXES_LOCKOUT_URL = '/users/locked'
AXES_LOCKOUT_PARAMETERS = [["ip_address", "user_agent"]]
AXES_RESET_ON_SUCCESS = True


# =============================================================================
# 8. Настройки CSP (Content Security Policy)
# 8. CSP (Content Security Policy) settings
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
# 9. Production settings
# =============================================================================

if not DEBUG:
    # Настройки HTTPS / HTTPS settings
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Настройки HSTS / HSTS settings
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Политика Referrer / Referrer policy
    SECURE_REFERRER_POLICY = 'same-origin'

    # Защита от кликджекинга / Clickjacking protection
    SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'

    # Оптимизация CSP / CSP optimization
    CONTENT_SECURITY_POLICY['DIRECTIVES'].update({
        'script-src': ["'self'", "https://cdn.jsdelivr.net"],
        'style-src': ["'self'", "https://cdn.jsdelivr.net"],
        'worker-src': ["'self'"],
    })
