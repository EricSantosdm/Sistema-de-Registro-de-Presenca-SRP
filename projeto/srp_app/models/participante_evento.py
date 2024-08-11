from django.contrib.auth.models import User
from django.db import models
from novadata_utils.models import AbstractNovadataModel

from .evento import Evento


class ParticipanteEvento(AbstractNovadataModel):
    evento = models.ForeignKey(
        to=Evento,
        verbose_name="Evento",
        null=True,
        on_delete=models.SET_NULL,
    )

    usuario = models.ForeignKey(
        to=User,
        verbose_name="Usuário",
        null=True,
        on_delete=models.SET_NULL,
    )

    presenca = models.BooleanField(
        verbose_name="Presença",
        default=False,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        presente = (
            "estava presente" if self.presenca else "não estava presente"
        )
        return f"{self.evento} - Usuário {self.usuario} {presente}"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "srp_app"
        verbose_name = "Participante do evento"
        verbose_name_plural = "Participantes do evento"
