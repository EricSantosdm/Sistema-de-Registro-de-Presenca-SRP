from django.db import models
from novadata_utils.models import AbstractNovadataModel


class Evento(AbstractNovadataModel):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    descricao = models.TextField(
        verbose_name="Descrição",
    )

    data_inicial = models.DateTimeField(
        verbose_name="Data inicial",
    )

    data_final = models.DateTimeField(
        verbose_name="Data final",
        null=True,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return str(self.nome)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "srp_app"
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
