
# Sistema de Registro de Presença (SRP)

## Descrição

O Sistema de Registro de Presença (SRP) é uma aplicação desenvolvida para facilitar o controle de frequência em eventos, reuniões e outras atividades. Utilizando tecnologia de QR Code, o sistema permite um registro rápido e preciso das presenças dos participantes.

## Funcionalidades

- Registro de presença via QR Code
- Geração de relatórios de frequência
- Controle de participantes em eventos e reuniões
- Interface amigável e fácil de usar
- Notificações e alertas de presença

## Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django
- **Banco de Dados:** PostgreSQL
- **Outros:** QR Code API, JWT para autenticação

## Instalação

1. Clone o repositório:
    ```sh
    https://github.com/EricSantosdm/Sistema-de-Registro-de-Presenca-SRP.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd srp
    ```
3. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```
4. Ative o ambiente virtual:

    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No MacOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
6. Configure as variáveis de ambiente no arquivo `.env`:
    ```sh
    SECRET_KEY=sua_chave_secreta
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=postgres://usuario:senha@localhost:5432/srp
    ```
7. Execute as migrações:
    ```sh
    python manage.py migrate
    ```
8. Crie um superusuário:
    ```sh
    python manage.py createsuperuser
    ```
9. Inicie o servidor:
    ```sh
    python manage.py runserver
    ```

## Como Usar

1. Acesse a aplicação no navegador através do endereço `http://localhost:8000`.
2. Faça login ou registre-se na plataforma.
3. Crie um evento ou reunião e gere os QR Codes para os participantes.
4. Os participantes podem escanear os QR Codes para registrar sua presença.
5. Acompanhe os registros de presença e gere relatórios conforme necessário.

## Equipe

- **Alysson Milanez** - Orientador
- **Bruno**
- **Dimona**
- **Eric**
- **Flavio**
- **Natalia**

## Contribuição

Se você deseja contribuir com o projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para sua feature:
    ```sh
    git checkout -b minha-feature
    ```
3. Commit suas alterações:
    ```sh
    git commit -m 'Adiciona minha feature'
    ```
4. Faça push para a branch:
    ```sh
    git push origin minha-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Se precisar de mais alguma informação ou ajustes, estou à disposição!
