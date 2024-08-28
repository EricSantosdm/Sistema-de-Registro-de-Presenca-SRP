from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from novadata_utils.redirect import reverse_lazy_plus
from srp_app.models import Evento, ParticipanteEvento


@login_required
def inscreverse(request, id_evento):
    """Faz a inscrição de um usuário no evento da url."""
    evento = get_object_or_404(Evento, id=id_evento)
    ParticipanteEvento.objects.create(evento=evento, usuario=request.user)

    return reverse_lazy_plus("home")
