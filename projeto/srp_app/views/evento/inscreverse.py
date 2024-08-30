from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from novadata_utils.redirect import reverse_lazy_plus
from srp_app.models import Evento, ParticipanteEvento


@login_required
def inscreverse(request, id_evento):
    """
    Faz a inscrição de um usuário no evento da url.

    Regra 1: Se o usuário já for participante do evento, não faz nada.
    """
    evento = get_object_or_404(Evento, id=id_evento)

    if evento.usuario_atual_inscrito:
        return reverse_lazy_plus(
            "ja_inscrito",
            url_params=[evento.id],
        )

    ParticipanteEvento.objects.create(evento=evento, usuario=request.user)
    return reverse_lazy_plus(
        "sucesso_inscricao",
        url_params=[evento.id],
    )
