# DATABASES
DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'zartek',
            'USER': 'postgres',
            'PASSWORD': 'ironman789',
            'HOST': 'localhost',
            'PORT': '5432',
       }
}


# REST
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}


# Swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

