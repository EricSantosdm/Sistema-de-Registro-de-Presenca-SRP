from django.contrib.auth.models import User
from django.db import models
from novadata_utils.models import AbstractNovadataModel


class Profile(AbstractNovadataModel, models.Model):
    usuario = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return f"{self.usuario}"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "home"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


User.add_to_class("__str__", User.get_full_name)
