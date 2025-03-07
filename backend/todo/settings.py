from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-%8ec%i^c!cptd52bok8qcoc&$=ucazz4mec75q4s87@h0%4fis'
DEBUG = True

# These are the hosts we allow to access our app, local dev setup for now
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

# List of all the installed apps, including Django default apps and our custom ones
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",  # This is for our API setup
    "corsheaders",  # For handling CORS
    "todo",  # This is our app for managing to-dos
]

# Middleware stack, includes CORS for frontend-backend communication
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Make sure this is above CommonMiddleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Frontend will run on port 8084, so we allow that in CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8084",
]

# Allow credentials (important if we're using authentication)
CORS_ALLOW_CREDENTIALS = True

# Let all headers and methods be accepted by the API
CORS_ALLOW_ALL_HEADERS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

# URL configuration for our app
ROOT_URLCONF = 'todo.urls'

# Django templates setup, not really used here but leaving for potential future use
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'todo.wsgi.application'

# Database configuration - for now, it's using SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation setup (keeping things secure)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Timezone settings for the app
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files config - we'll serve these during development
STATIC_URL = 'static/'

# Default primary key type, leaving it as BigAutoField for now
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
