from django.views.generic import DetailView
from srp.views import AdminContextMixin

from ...models import Evento


class SucessoPresencaView(AdminContextMixin, DetailView):
    template_name = "admin/sucesso_presenca.html"

    model = Evento

    def get_context_data(self, **kwargs):
        """Retorna o contexto da view."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Presença registrada com sucesso."

        return context
