from django.apps import AppConfig


class StudentConfig(AppConfig):
    """
    Configuration class for the Student app.

    This class defines the configuration for the Student app, including the app's name and default auto-generated
    primary key field.

    Attributes:
        .default_auto_field (str): The name of the default auto-generated primary key field for models in this app.
        .name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Student'
