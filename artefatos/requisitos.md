# Requisitos do Sistema de Registro de Presença (SRP)

## Requisitos Funcionais

### RF01 - Registro de Presença via QR Code
**Descrição:** O sistema deve permitir que os participantes registrem sua presença escaneando um QR Code exclusivo.
- **Critérios de Aceitação:**
  - O QR Code deve ser gerado automaticamente para cada evento ou reunião.
  - O sistema deve confirmar o registro com uma mensagem de sucesso na interface do usuário.
  - O registro de presença deve ser armazenado no banco de dados em tempo real.

### RF02 - Geração de Relatórios de Frequência
**Descrição:** O sistema deve gerar relatórios de frequência para cada evento ou reunião.
- **Critérios de Aceitação:**
  - Os relatórios devem incluir a lista completa de participantes, horários de chegada e porcentagem de presença.
  - O usuário deve poder exportar os relatórios em formato PDF ou Excel.
  - O sistema deve permitir a filtragem dos relatórios por data, evento e participante.

### RF03 - Controle de Participantes
**Descrição:** O sistema deve permitir o cadastro, edição e exclusão de participantes para eventos e reuniões.
- **Critérios de Aceitação:**
  - O cadastro de novos participantes deve requerer campos obrigatórios como nome, e-mail e identificação única.
  - O sistema deve validar a unicidade do e-mail e da identificação antes de cadastrar um participante.
  - O sistema deve permitir a busca de participantes por nome ou e-mail.

### RF04 - Cadastro Manual de Presença
**Descrição:** O sistema deve permitir que a presença de um participante seja registrada manualmente pelo administrador.
- **Critérios de Aceitação:**
  - O administrador deve poder buscar o participante pelo nome ou identificação.
  - O registro manual deve ser registrado no banco de dados com a data e hora corretas.
  - O sistema deve registrar quem efetuou o cadastro manual.

### RF05 - Cadastro de Usuários
**Descrição:** O sistema deve permitir o cadastro de diferentes usuários com níveis de acesso distintos (administradores e participantes).
- **Critérios de Aceitação:**
  - O cadastro deve requerer nome, e-mail, senha e tipo de usuário (administrador ou participante).
  - O sistema deve garantir que apenas administradores possam cadastrar novos usuários.
  - Senhas devem ser armazenadas de forma criptografada.

### RF06 - Interface Amigável
**Descrição:** O sistema deve possuir uma interface de usuário intuitiva e de fácil navegação.
- **Critérios de Aceitação:**
  - O usuário deve conseguir acessar todas as funcionalidades principais em até 3 cliques a partir da tela inicial.
  - Elementos da interface devem ser consistentes em todas as páginas (e.g., botões, fontes).
  - A interface deve ser responsiva, ajustando-se a diferentes tamanhos de tela.

## Requisitos Não Funcionais

### RNF01 - Desempenho
**Descrição:** O sistema deve ter um tempo de resposta inferior a 2 segundos para todas as operações.
- **Critérios de Aceitação:**
  - Testes de carga devem demonstrar que o sistema atende a este requisito sob condições normais de uso.

### RNF02 - Segurança
**Descrição:** O sistema deve garantir a segurança dos dados dos usuários e participantes.
- **Critérios de Aceitação:**
  - Todos os dados sensíveis (e.g., senhas) devem ser criptografados.
  - O sistema deve implementar autenticação por dois fatores (2FA) para administradores.
  - A aplicação deve ser protegida contra ataques comuns como SQL Injection e Cross-Site Scripting (XSS).

### RNF03 - Disponibilidade
**Descrição:** O sistema deve estar disponível 99,9% do tempo, exceto em períodos de manutenção programada.
- **Critérios de Aceitação:**
  - O sistema deve ter uma arquitetura redundante para garantir alta disponibilidade.
  - Logs de uptime e downtime devem ser gerados e revisados regularmente.

### RNF04 - Manutenibilidade
**Descrição:** O sistema deve ser fácil de manter e atualizar.
- **Critérios de Aceitação:**
  - O código deve ser bem documentado e seguir padrões de codificação reconhecidos.
  - Mudanças no código não devem exigir mais de 1 hora para serem integradas e testadas.
  - O sistema deve suportar atualizações sem perda de dados.

### RNF05 - Escalabilidade
**Descrição:** O sistema deve ser capaz de escalar para suportar um aumento no número de usuários e eventos.
- **Critérios de Aceitação:**
  - A arquitetura do sistema deve permitir a adição de novos servidores para balanceamento de carga.
  - O desempenho deve ser mantido dentro dos limites aceitáveis com até 10.000 usuários simultâneos.
