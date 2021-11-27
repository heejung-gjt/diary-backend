from pathlib import Path
import environ, os


env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

ALGORITHM = 'HS256'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    # "django.contrib.admin",
    # "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "diary",
    "user",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    # "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                # "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("NAME"),
        "USER": env("NAME"),
        "PASSWORD": env("PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('NAME'),
#         'USER': 'diary',
#         'PASSWORD': env('PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '',

#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'


USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

##CORS
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "access-control-allow-headers",
    "access-control-allow-methods",
    "access-control-allow-origin",
    "authorization",
    "content-type"
)

# s3 설정
AWS_ACCESS_KEY_ID=env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME="ap-northeast-2" # 버킷 생성할때 지정한 region을 작성한다
AWS_S3_FILE_OVERWRITE=False # 기본적인 오버라이트 설정 false

# import dj_database_url

# db_from_env = dj_database_url.config(conn_max_age=500)

# DATABASES['default'].update(db_from_env)

APPEND_SLASH = False
