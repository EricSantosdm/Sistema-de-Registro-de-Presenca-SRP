from django.db import models
from novadata_utils.models import AbstractNovadataModel


class Visitante(AbstractNovadataModel):
    nome_completo = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return str(self.nome_completo)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "srp_app"
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
