**Desafio DIO - Criando um Sistema Bancário com Python**

_Objetivo Geral_  
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

_Desafio_  
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

- Operação de depósito: Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- Operação de saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

- Operação de extrato: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
  Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

**Desafio DIO - Criando um Sistema Bancário com Python Pt. 2**

_Objetivo Geral_  
Exercitar o novo conhecimento sobre data e hora implementando funcionalidades sobre esse tema. Seguindo versionamento: v0.2

_Desafio_  
Implementar funcionalidade de data e hora no sistema feito anteriormente onde:

- Deverá ser estabelecido um limite de 10 transações diárias para a conta.
- Se o usuário tentar fazer uma transação após o limite, ele deverá ser informado que excedeu o limite daquele dia.
- Mostrar no extrato a data e a hora de todas as transações.

**Desafio DIO - Criando um Sistema Bancário com Python Pt. 2.1**

_Objetivo Geral_  
Modularização das funções existentes e criação de dois novos métodos: criar usuario e criar conta. Seguindo versionamento: v0.21

_Desafio_  
Realizar a separação de cada umas das funções preexistentes (depositar, saque e extrato), e para exercitar o que foi aprendido em modulos anteriores aplicar as seguintes regras:

- Os argumentos da função sacar devem ser _keyword only_. Argumentos sugeridos: saldo, valor, extrato, limite, n_saques, limite_saques. Sugestão de retorno: saldo e extrato.
- Os argumentos da função depositar devem ser _position only_. Argumentos sugeridos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
- Os argumentos da função extrato devem ser parte _keyword only_ e parte _position only_. Sugestão de argumentos posicionais: saldo. Sugestão de argumentos por palavra chave: extrato.

Em seguida, adicionar ao escopo mais duas funções: criar usuario e criar conta, onde:

- Um usuário deverá ser registrado em uma lista e é composto por: nome, data de nascimento, cpf - sem os pontos e traços - e endereço, no qual este último deve ser formatado: logradouro, número - bairro - cidade/sigla do estado. Não pode se registrar dois usuários com o mesmo número de CPF.

- Uma conta será registrada em uma lista e sua composição é: agência (que será padrão para todas contas o código "0001"), numero da conta que será auto-incremental, inicializando em 1 e um usuário.

- Um usuário poder ter zero ou mais contas e uma conta deve ser de um usuário.
