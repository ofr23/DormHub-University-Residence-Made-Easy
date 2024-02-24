from django.apps import AppConfig


class StaffConfig(AppConfig):
    """
    AppConfig class for the Staff app.

    This class defines the configuration for the Staff app,
    including the default auto field for models.

    Attributes:
        .default_auto_field (str): The default auto field for models.
        .name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Staff'
