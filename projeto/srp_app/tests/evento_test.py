from datetime import datetime

from django.contrib.auth.models import User
from django.test import Client, TestCase
from srp_app.models import Evento, Visitante


class EventoTest(TestCase):
    def setUp(self):
        """Faz os preparativos para os testes de eventos."""
        visitante_data = {"nome_completo": "Visitante 1"}
        self.visitante = Visitante.objects.create(**visitante_data)

        evento_data = {
            "nome": "Evento 1",
            "descricao": "Descrição 1",
            "data_inicial": datetime.now().date(),
            "data_final": datetime.now().date(),
        }
        self.evento = Evento.objects.create(**evento_data)

        self.client = Client()
        self.usuario = User.objects.create_user(
            username="user1", password="senha123"
        )
        self.client.login(username="user1", password="senha123")

    def test_create(self):
        """Testa a criação de um objeto."""
        horario_agora = datetime.now().date()

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

    def test_update(self):
        """Testa a atualização de um objeto."""
        horario_agora = datetime.now().date()

        evento = Evento.objects.create(
            nome="Evento 1",
            descricao="Descrição 1",
            data_inicial=horario_agora,
            data_final=horario_agora,
        )
        evento.visitantes.add(self.visitante)

        evento.nome = "Evento 2"
        evento.descricao = "Descrição 2"
        evento.data_inicial = horario_agora
        evento.data_final = horario_agora
        evento.save()

        self.assertEqual(evento.nome, "Evento 2")
        self.assertEqual(evento.descricao, "Descrição 2")
        self.assertEqual(evento.data_inicial, horario_agora)
        self.assertEqual(evento.data_final, horario_agora)
        self.assertEqual(evento.visitantes.first(), self.visitante)

    def test_delete(self):
        """Testa a exclusão de um objeto."""
        horario_agora = datetime.now().date()

        self.assertEqual(Evento.objects.count(), 1)

        evento = Evento.objects.create(
            nome="Evento 1",
            descricao="Descrição 1",
            data_inicial=horario_agora,
            data_final=horario_agora,
        )

        self.assertEqual(Evento.objects.count(), 2)
        evento.delete()
        self.assertEqual(Evento.objects.count(), 1)

    def test_str(self):
        """Testa a representação de um objeto."""
        horario_agora = datetime.now().date()

        evento = Evento.objects.create(
            nome="Evento 1",
            descricao="Descrição 1",
            data_inicial=horario_agora,
            data_final=horario_agora,
        )

        self.assertEqual(str(evento), "Evento 1")

    def test_inscreverse(self):
        """Testa a inscrição de um usuário em um evento."""

        self.assertFalse(self.evento.usuario_atual_inscrito)
        self.client.post(
            f"http://localhost:8000/srp_app/inscreverse/{self.evento.id}",
            timeout=2,
        )
        self.assertTrue(self.evento.usuario_atual_inscrito)
