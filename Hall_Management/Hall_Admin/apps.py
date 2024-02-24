from django.apps import AppConfig


class HallAdminConfig(AppConfig):
    """
    AppConfig class for configuring the Hall_Admin app.
    """
    # Define the default_auto_field attribute
    default_auto_field = 'django.db.models.BigAutoField'

    # Define the name attribute
    name = 'Hall_Admin'
