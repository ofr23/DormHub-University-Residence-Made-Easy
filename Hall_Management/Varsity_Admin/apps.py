from django.apps import AppConfig


class VarsityAdminConfig(AppConfig):
    # A class attribute specifying the default auto field to use for models in the app.
    default_auto_field = 'django.db.models.BigAutoField'

    # A class attribute specifying the name of the app.
    name = 'Varsity_Admin'
