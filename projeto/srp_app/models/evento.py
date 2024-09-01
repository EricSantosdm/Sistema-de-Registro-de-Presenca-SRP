from crum import get_current_user
from django.db import models
from novadata_utils.models import AbstractNovadataModel

from .visitante import Visitante


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

    visitantes = models.ManyToManyField(
        to=Visitante,
        verbose_name="Visitantes",
        blank=True,
    )

    @property
    def usuario_atual_inscrito(self):
        """Informa se o usuário atual está inscrito no evento."""
        return self.participanteevento_set.filter(
            usuario=get_current_user()
        ).exists()

    @property
    def usuario_atual_presenca(self):
        """Informa se o usuário atual está com presença marcada no evento."""
        return self.participanteevento_set.filter(
            usuario=get_current_user(),
            presenca=True,
        ).exists()

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return str(self.nome)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "srp_app"
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
