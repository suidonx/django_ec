from .base import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", ".herokuapp.com"]

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",
    "items.apps.ItemsConfig",
    "manage_items.apps.ManageItemsConfig",
    "carts.apps.CartsConfig",
    "checkouts.apps.CheckoutsConfig",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
