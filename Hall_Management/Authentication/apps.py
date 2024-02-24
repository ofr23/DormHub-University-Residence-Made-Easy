from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    AppConfig class for configuring the Authentication app.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Sets the default primary key type
    name = 'Authentication'  # Name of the app
