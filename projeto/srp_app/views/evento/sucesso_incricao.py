from django.views.generic import DetailView
from srp.views import AdminContextMixin

from ...models import Evento


class SucessoInscricaoView(AdminContextMixin, DetailView):
    template_name = "admin/sucesso_inscricao.html"

    model = Evento

    def get_context_data(self, **kwargs):
        """Retorna o contexto da view."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Inscrição realizada com sucesso."

        return context
