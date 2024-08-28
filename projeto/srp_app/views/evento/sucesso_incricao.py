from django.views.generic import DetailView
from srp_app.models import Evento


class SucessoInscricaoView(DetailView):
    template_name = "home/sucesso_inscricao.html"

    model = Evento
