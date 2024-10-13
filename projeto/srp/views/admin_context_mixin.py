from django.contrib.admin.sites import site as admin_site


class AdminContextMixin:
    def get_context_data(self, **kwargs):
        """Retorna o contexto da view."""
        context = super().get_context_data(**kwargs)
        admin_context = admin_site.each_context(self.request)
        context.update(admin_context)

        return context
