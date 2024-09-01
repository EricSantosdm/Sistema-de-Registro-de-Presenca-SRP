# Requisitos do Sistema de Registro de Presença (SRP)

## Requisitos Funcionais
----
----

### RF01
**Nome:** Registro de Presença via QR Code

**Descrição:** Permitir que os participantes registrem sua presença escaneando um QR Code exclusivo gerado pelo sistema.

**Atores:** Participantes, Administradores

**Prioridade:** Alta

**Anexo:** Nenhum

----

**Entradas e pré-condições:**
- O QR Code deve ser gerado pelo sistema e estar disponível para o participante.
- O participante deve ter acesso a um dispositivo com câmera para escanear o QR Code.

**Saídas e pós-condições:**
- O sistema registra a presença do participante e exibe uma mensagem de confirmação.
- O registro é armazenado no banco de dados com data e hora.

**Fluxos de eventos**
**Fluxo principal:**
1. O participante acessa a página do evento e escaneia o QR Code.
2. O sistema valida o QR Code e registra a presença.
3. O sistema confirma o registro e armazena a informação no banco de dados.

**Fluxo secundário 1:**
- O participante tenta escanear um QR Code inválido.
  1. O sistema exibe uma mensagem de erro indicando que o QR Code não é válido.
----
----
### RF02
**Nome:** Geração de Relatórios de Frequência

**Descrição:** Gerar relatórios de frequência detalhados para cada evento ou reunião, permitindo exportação em PDF ou Excel.

**Atores:** Administradores

**Prioridade:** Média

**Anexo:** Nenhum

----

**Entradas e pré-condições:**
- Eventos ou reuniões devem ter registros de presença armazenados no sistema.

**Saídas e pós-condições:**
- Relatório gerado contendo a lista de participantes, horários de chegada e porcentagem de presença.

**Fluxos de eventos**
**Fluxo principal:**
1. O administrador seleciona o evento ou reunião para o qual deseja gerar o relatório.
2. O sistema processa os dados e gera o relatório.
3. O administrador escolhe o formato (PDF ou Excel) e baixa o relatório.

**Fluxo secundário 1:**
- O administrador tenta gerar um relatório para um evento sem registros de presença.
  1. O sistema informa que não há dados suficientes para gerar o relatório.
----
----
### RF03
**Nome:** Controle de Participantes

**Descrição:** Permitir o cadastro, edição e exclusão de participantes para eventos e reuniões.

**Atores:** Administradores

**Prioridade:** Alta

**Anexo:** Nenhum

----

**Entradas e pré-condições:**
- O administrador deve estar autenticado no sistema.

**Saídas e pós-condições:**
- O participante é cadastrado, editado ou excluído conforme a ação do administrador.

**Fluxos de eventos**
**Fluxo principal:**
1. O administrador acessa o módulo de controle de participantes.
2. O administrador insere ou edita os dados do participante (nome, e-mail, identificação).
3. O sistema valida os dados e confirma a ação.

**Fluxo secundário 1:**
- O administrador tenta cadastrar um participante com e-mail duplicado.
  1. O sistema exibe uma mensagem de erro indicando que o e-mail já está em uso.
----
----
### RF04
**Nome:** Cadastro Manual de Presença

**Descrição:** Permitir que o administrador registre manualmente a presença de um participante.

**Atores:** Administradores

**Prioridade:** Média

**Anexo:** Nenhum

----

**Entradas e pré-condições:**
- O administrador deve ter os dados do participante (nome ou identificação) para realizar o cadastro manual.

**Saídas e pós-condições:**
- O sistema registra manualmente a presença do participante com data e hora.

**Fluxos de eventos**
**Fluxo principal:**
1. O administrador acessa a opção de cadastro manual de presença.
2. O administrador busca o participante pelo nome ou identificação.
3. O sistema registra a presença com a data e hora atuais.

**Fluxo secundário 1:**
- O administrador não encontra o participante pelo nome ou identificação.
  1. O sistema exibe uma mensagem de erro indicando que o participante não foi encontrado.
----
----
### RF05
**Nome:** Cadastro de Usuários

**Descrição:** Permitir o cadastro de novos usuários com diferentes níveis de acesso (administradores e participantes).

**Atores:** Administradores

**Prioridade:** Alta

**Anexo:** Nenhum

----

**Entradas e pré-condições:**
- O administrador deve estar autenticado no sistema.

**Saídas e pós-condições:**
- O usuário é cadastrado no sistema com senha criptografada e nível de acesso adequado.

**Fluxos de eventos**
**Fluxo principal:**
1. O administrador acessa o módulo de cadastro de usuários.
2. O administrador insere os dados do usuário (nome, e-mail, senha, tipo de usuário).
3. O sistema valida os dados e confirma o cadastro.

**Fluxo secundário 1:**
- O administrador tenta cadastrar um usuário com e-mail duplicado.
  1. O sistema exibe uma mensagem de erro indicando que o e-mail já está em uso.
----
----
### RF06
**Nome:** Interface Amigável

**Descrição:** Oferecer uma interface de usuário intuitiva e de fácil navegação para todas as funcionalidades do sistema.

**Atores:** Todos os usuários

**Prioridade:** Alta

**Anexo:** Nenhum

----

**Entradas e pré-condições:**
- O sistema deve estar em operação.

**Saídas e pós-condições:**
- O usuário navega pelas funcionalidades principais do sistema com facilidade.

**Fluxos de eventos**
**Fluxo principal:**
1. O usuário acessa a página inicial do sistema.
2. O usuário navega pelas opções disponíveis com no máximo 3 cliques.
3. O sistema responde de forma eficiente, exibindo as informações solicitadas.

**Fluxo secundário 1:**
- O usuário acessa o sistema em um dispositivo com tela menor.
  1. O sistema ajusta automaticamente a interface para o tamanho da tela, mantendo a usabilidade.
----
----
## Requisitos Não Funcionais
----
----
### RNF01
**Nome:** Desempenho

**Descrição:** O sistema deve responder em menos de 2 segundos para todas as operações realizadas.

**Atores:** Todos os usuários

**Prioridade:** Alta

**Anexo:** Logs de desempenho

----

**Entradas e pré-condições:**
- O sistema deve estar em operação normal.

**Saídas e pós-condições:**
- As operações realizadas pelos usuários são concluídas dentro do tempo especificado.

**Fluxos de eventos**
**Fluxo principal:**
1. O usuário realiza uma operação (e.g., registro de presença, geração de relatório).
2. O sistema processa a operação e retorna a resposta em menos de 2 segundos.

**Fluxo secundário 1:**
- A operação leva mais de 2 segundos para ser concluída.
  1. O sistema gera um log de desempenho e alerta o administrador.
----
----
### RNF02
**Nome:** Segurança

**Descrição:** Garantir a proteção dos dados dos usuários e participantes contra acessos não autorizados e vulnerabilidades.

**Atores:** Todos os usuários

**Prioridade:** Alta

**Anexo:** Logs de segurança

----

**Entradas e pré-condições:**
- O sistema deve estar em operação e os usuários devem estar autenticados.

**Saídas e pós-condições:**
- Os dados sensíveis são protegidos e o acesso ao sistema é controlado.

**Fluxos de eventos**
**Fluxo principal:**
1. O usuário acessa o sistema e realiza login.
2. O sistema verifica as credenciais e autentica o usuário.
3. O sistema criptografa todas as informações sensíveis e protege contra ataques comuns.

**Fluxo secundário 1:**
- O sistema detecta uma tentativa de ataque (e.g., SQL Injection).
  1. O sistema bloqueia a tentativa e alerta o administrador.
----
----
### RNF03
**Nome:** Disponibilidade

**Descrição:** O sistema deve estar disponível para uso 99,9% do tempo, exceto durante manutenções programadas.

**Atores:** Todos os usuários

**Prioridade:** Alta

**Anexo:** Logs de uptime

----

**Entradas e pré-condições:**
- O sistema deve estar em operação e monitorado.

**Saídas e pós-condições:**
- O sistema mantém alta disponibilidade, com interrupções mínimas.

**Fluxos de eventos**
**Fluxo principal:**
1. O usuário acessa o sistema durante o horário de operação.
2. O sistema está disponível e funcionando corretamente.

**Fluxo secundário 1:**
- O sistema entra em modo de manutenção programada.
  1. O sistema exibe uma mensagem informando o período de manutenção e quando estará disponível novamente.
----
----
### RNF04
**Nome:** Manutenibilidade

**Descrição:** O sistema deve ser fácil de manter e atualizar, com código bem documentado e modular.

**Atores:** Equipe de Desenvolvimento

**Prioridade:** Média

**Anexo:** Documentação do código

----

**Entradas e pré-condições:**
- O sistema deve estar em operação e a equipe de desenvolvimento deve ter acesso ao código.

**Saídas e pós-condições:**
- As atualizações e correções são implementadas rapidamente sem comprometer a integridade do sistema.

**Fluxos de eventos**
**Fluxo principal:**
1. A equipe de desenvolvimento identifica uma necessidade de atualização ou correção.
2. A equipe realiza a atualização, seguindo a documentação e padrões de codificação.
3. O sistema é atualizado e testado sem impacto negativo nas operações.

**Fluxo secundário 1:**
- Uma atualização falha durante a implementação.
  1. A equipe reverte para a versão anterior e investiga a causa do problema.
----
----
### RNF05
**Nome:** Escalabilidade

**Descrição:** O sistema deve ser capaz de escalar para suportar um aumento no número de usuários e eventos sem perda de desempenho.

**Atores:** Administradores, Equipe de Desenvolvimento

**Prioridade:** Média

**Anexo:** Arquitetura de sistema

----

**Entradas e pré-condições:**
- O sistema deve estar projetado para escalabilidade desde o início.

**Saídas e pós-condições:**
- O sistema mantém desempenho eficiente mesmo com aumento significativo de usuários.

**Fluxos de eventos**
**Fluxo principal:**
1. O número de usuários e eventos no sistema aumenta significativamente.
2. O sistema distribui a carga e continua a operar dentro dos parâmetros de desempenho.

**Fluxo secundário 1:**
- A carga excede a capacidade atual do sistema.
  1. O sistema alerta os administradores para a necessidade de expansão de infraestrutura.
----
----
