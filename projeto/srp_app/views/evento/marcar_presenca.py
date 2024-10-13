from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from novadata_utils.redirect import reverse_lazy_plus
from srp_app.models import Evento, ParticipanteEvento


@login_required
def marcar_presenca(request, id_evento):
    """
    Marca a presença de um usuário no evento da url.

    Regra 1: Se o usuário já tiver presença, não faz nada.
    Regra 2: Se o usuário não for inscrito no evento,
    o inscreve e marca a presença.
    """
    evento = get_object_or_404(Evento, id=id_evento)

    if evento.usuario_atual_inscrito:
        if evento.usuario_atual_presenca:
            return reverse_lazy_plus(
                "sucesso_presenca",
                url_params=[evento.id],
            )

        ParticipanteEvento.objects.filter(
            evento=evento,
            usuario=request.user,
        ).update(presenca=True)
    else:
        return reverse_lazy_plus(
            "inscreverse",
            url_params=[evento.id],
        )

    return reverse_lazy_plus(
        "sucesso_presenca",
        url_params=[evento.id],
    )
