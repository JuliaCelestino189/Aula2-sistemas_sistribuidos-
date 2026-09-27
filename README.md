# Aula2-sistemas_sistribuidos-

Nesta aula, foram estudados os principais modelos de arquitetura em sistemas distribuídos e seus desafios, como concorrência, escalabilidade e falhas.

### Arquitetura Cliente-Servidor

O cliente solicita serviços e o servidor processa as solicitações e fornece as respostas. Esse modelo facilita o gerenciamento e a centralização dos recursos, mas pode apresentar problemas de sobrecarga e ponto único de falha.

### Arquitetura P2P

No modelo **Peer-to-Peer (P2P)**, os participantes podem atuar tanto como clientes quanto como fornecedores de recursos, sem uma divisão rígida entre cliente e servidor.

### Arquitetura em Três Camadas

Divide o sistema em:

* Apresentação: interface do usuário;
* Aplicação: regras e lógica do sistema;
* Dados: armazenamento das informações.

### Escalabilidade

É a capacidade de um sistema suportar o aumento de usuários, requisições ou dados. O balanceamento de carga pode ser utilizado para distribuir as solicitações entre diferentes servidores.

## 💻 Atividade Prática

Foi implementada uma comunicação Cliente-Servidor utilizando Sockets em Python. O servidor foi configurado para aguardar conexões na porta 5000, enquanto o cliente estabeleceu a conexão e enviou uma mensagem.

A atividade demonstrou, na prática, como dois processos podem se comunicar através de uma rede utilizando Sockets e o protocolo TCP/IP.
