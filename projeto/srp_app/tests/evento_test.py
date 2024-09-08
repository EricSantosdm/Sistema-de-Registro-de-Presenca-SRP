from datetime import datetime

from django.test import TestCase
from srp_app.models import Evento, Visitante


class EventoTest(TestCase):
    def setUp(self):
        """Faz os preparativos para os testes de eventos."""
        visitante_data = {"nome_completo": "Visitante 1"}
        self.visitante = Visitante.objects.create(**visitante_data)

    def test_create(self):
        """Testa a criação de um objeto."""
        horario_agora = datetime.now()

        evento = Evento.objects.create(
            nome="Evento 1",
            descricao="Descrição 1",
            data_inicial=horario_agora,
            data_final=horario_agora,
        )
        evento.visitantes.add(self.visitante)

        self.assertEqual(evento.nome, "Evento 1")
        self.assertEqual(evento.descricao, "Descrição 1")
        self.assertEqual(evento.data_inicial, horario_agora)
        self.assertEqual(evento.data_final, horario_agora)
        self.assertEqual(evento.visitantes.first(), self.visitante)
