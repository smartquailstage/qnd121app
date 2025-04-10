from .base_prod import *
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _



DEBUG=True


# Obtener las variables de entorno desde Kubernetes
IP = os.environ.get("IP")
DOMAIN = os.environ.get("DOMAIN")
HOST = os.environ.get("HOST")


ALLOWED_HOSTS = ['127.0.0.1','localhost','agrosylma.smartquail.io', '146.190.0.47', '*']


#import wagtail_ai

#WAGTAIL_AI_PROMPTS = wagtail_ai.DEFAULT_PROMPTS + [
#    {
#        "label": "Simplify",
#        "description": "Rewrite your text in a simpler form",
#        "prompt": "Rewrite the following text to make it simper and more succinct",
#        "method": "replace",
#    }
#]


CSRF_COOKIE_DOMAIN="agrosylma.smartquail.io"
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://agrosylma.smartquail.io/','https://146.190.0.47']
CORS_ALLOWED_ORIGINS = [
    'https://agrosylma.smartquail.io/asmerp/','https://agrosylma.smartquail.io/pedidos/ingresar'
    # Otros orígenes permitidos si los hay
]



#import wagtail_ai

#WAGTAIL_AI_PROMPTS = wagtail_ai.DEFAULT_PROMPTS + [
#    {
#        "label": "Simplify",
#        "description": "Rewrite your text in a simpler form",
#        "prompt": "Rewrite the following text to make it simper and more succinct",
#        "method": "replace",
#    }
#]


#CSRF_COOKIE_DOMAIN=".www.smartquail.io"
#CSRF_COOKIE_SECURE = True
#CSRF_TRUSTED_ORIGINS = ['https://www.smartquail.io','https://146.190.164.22']
#CORS_ALLOWED_ORIGINS = [
#    'https://www.smartquail.io','https://146.190.164.22'
#    # Otros orígenes permitidos si los hay
#]



UNFOLD = {
    "SITE_TITLE": "AGROSILMA - Sistema Operativo ERP",
    "SITE_HEADER": "Agro Sylvia María",
    "SITE_SUBHEADER": "Sistema Operativo - ERP",

    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("assets/images/logo_test.png"),
        "dark": lambda request: static("assets/images/logo_test.png"),
    },
    "SITE_LOGO": {
        "light": lambda request: static("assets/images/logo_test.png"),
        "dark": lambda request: static("assets/images/logo_test.png"),
    },
    "SITE_SYMBOL": "speed",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("img/agro_logo.png"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": False,
    
    "ENVIRONMENT": "Production.environment_callback",
    "THEME": "dark",
    "LOGIN": {
        "image": lambda request: static("assets/images/BG3.jpg"),
       # "redirect_after": lambda request: reverse_lazy("admin:usuarios_changelist"),
    },
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "BORDER_RADIUS": "6px",
    "COLORS": {
        "base": {
            "50": "0, 180, 81",
            "100": "243 244 246",
            "200": "229 231 235",
            "300": "209 213 219",
            "400": "240 159 3",
            "500": "255 227 0",
            "600": "240 159 3",
            "700": "223 189 4",
            "800": "106 63 3",
            "900": "34 18 0",
            "950": "3 7 18",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "206 137 5",
            "600": "58 128 0",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
 "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Gestión de Usuarios"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Usuarios"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Grupo de Usuarios"),
                        "icon": "groups",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                                        {
                        "title": _("Perfil de Usuario"),
                        "icon": "list",
                        "link": reverse_lazy("admin:usuarios_profile_changelist"),
                    },
                ],
            },
            {
                "title": _("Bodega"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Categorias de productos"),
                        "icon": "package",
                        "link": reverse_lazy("admin:shop_category_changelist"),
                    },
                    {
                        "title": _("Item de productos"),
                        "icon": "package",
                        "link": reverse_lazy("admin:shop_product_changelist"),
                    },
                ],
            },
            {
                "title": _("Ventas"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Ordenes de Pedidos"),
                        "icon": "payment",
                        "link": reverse_lazy("admin:orders_order_changelist"),
                    },

                ],
            },

            {
                "title": _("Creditos"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Descuentos"),
                        "icon": "money",
                        "link": reverse_lazy("admin:coupons_coupon_changelist"),
                    },

                ],
            },
        ],
    },
 
    "MENU": [
        {
            "title": _("Dashboard"),
            "icon": "dashboard",
            "link": reverse_lazy("admin:index"),
            "permission": lambda request: request.user.is_superuser,
        },
        {
            "title": _("Users"),
            "icon": "people",
            "link": reverse_lazy("admin:auth_user_changelist"),
        },
    ],

}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Obtención de variables de entorno para la configuración de PostgreSQL
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_ENGINE = os.environ.get("POSTGRES_ENGINE")

# Verificación de disponibilidad de las variables necesarias para PostgreSQL
DB_IS_AVAILABLE = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

# Configuración condicional para PostgreSQL
if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': DB_DATABASE,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }

#Static files DevMod





from .cdn.conf import * #noqa




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery setup



#Email setups
EMAIL_HOST          = os.environ.get('EMAIL_HOST')
EMAIL_PORT          =  os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER ')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS       = False
#EMAIL_USE_SSL       = False


REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  

CELERY_BROKER_URL = 'amqp://support:ms95355672@rabbitmq:5672//'
#CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = 'pyamqp://support:ms95355672@rabbitmq:5672//'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET =  os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ')




CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
}
}


# Configuración de AWS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL")  # Cambia si usas otro endpoint
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"  # Cambia a 'private' si los archivos deben ser privados
}

# Configuración de almacenamiento
AWS_LOCATION = os.environ.get("AWS_LOCATION")  # 'static' o 'media'

# Asegúrate de que la URL de los archivos estáticos esté correcta
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'