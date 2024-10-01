from django.apps import AppConfig


class SrpAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "srp_app"
    verbose_name = "Sistema de registro de presença"

    def ready(self):
        import srp_app.signals
