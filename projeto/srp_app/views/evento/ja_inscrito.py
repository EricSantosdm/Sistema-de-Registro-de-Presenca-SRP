from django.views.generic import DetailView
from srp_app.models import Evento


class JaInscritoView(DetailView):
    template_name = "home/evento/ja_inscrito.html"

    model = Evento
