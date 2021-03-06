from django.apps import AppConfig
from django.core import management


class MusicConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "music"

    def ready(self):
        """Run migrations and create a superuser programatically."""
        management.call_command("makemigrations")
        management.call_command("migrate")
        management.call_command("createsuperuser", "--noinput")
