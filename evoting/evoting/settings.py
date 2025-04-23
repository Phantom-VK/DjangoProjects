from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------
# ✅ SECURITY SETTINGS
# --------------------

SECRET_KEY = 'x(lqudg86zj*qk#2wvr!vl#tr6=t57r%=v#&hmh+q&k@qkpk$5'  # Use env vars in production!

DEBUG = False  # Set to False for production

ALLOWED_HOSTS = ['*']  # Change to your domain for security

CSRF_TRUSTED_ORIGINS = [
    'https://djangoprojects-production.up.railway.app',
]

# --------------------------
# ✅ INSTALLED APPS
# --------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'voting',
    'corsheaders',  # ✅ CORS support
]

# --------------------------
# ✅ MIDDLEWARE
# --------------------------

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ Should be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# ✅ CORS SETTINGS
# --------------------------

CORS_ALLOWED_ORIGINS = [
    'https://djangoprojects-production.up.railway.app',
]

# --------------------------
# ✅ URL CONFIG
# --------------------------

ROOT_URLCONF = 'evoting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'evoting.wsgi.application'

# --------------------------
# ✅ DATABASE
# --------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------
# ✅ PASSWORD VALIDATION
# --------------------------

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

# --------------------------
# ✅ INTERNATIONALIZATION
# --------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------
# ✅ STATIC FILES SETTINGS
# --------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where collectstatic puts files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
