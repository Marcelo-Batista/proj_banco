from deposito import Deposito
from saque import Saque

LIMITE_SAQUE = 500
LIMITE_QUANT_SAQUES = 10
MENU = '''

[d] Depositar
[s] Sacar
[e] Extrato
[a] Abrir conta
[c] Criar usuário
[x] Sair

'''
def filtrar_clientes(clientes, cpf):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if len(clientes_filtrados) > 0 else None

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta.agencia} - Conta: {conta.conta}")
    
def filtrar_contas(contas, numero):
    contas_filtradas = [conta for conta in contas if conta.conta == numero]
    return contas_filtradas[0] if len(contas_filtradas) > 0 else None

def selecionar_cliente(clientes):
    cpf = input("Digite o CPF: ")
    cliente = filtrar_clientes(clientes, cpf)
    return cliente

def selecionar_conta(contas):
    if len(contas) < 1:
        print("Cliente não possui contas.")
        return
    listar_contas(contas)
    numero = input("Digite o número da conta: ")
    conta = filtrar_contas(contas, numero)
    return conta

def identificacao_cliente_conta(clientes):
    cliente = selecionar_cliente(clientes)
    if not cliente:
        print("Cliente não encontrado.")
        return
    
    conta = selecionar_conta(cliente.contas)
    if not conta:
        print("Conta não encontrada.")
        return
    
    return cliente, conta

def depositar(clientes):
    cliente, conta = identificacao_cliente_conta(clientes)   
    valor = float(input("Digite o valor a ser depositado: "))
    transacao = Deposito(valor)

    if cliente and conta and transacao:
        cliente.realizar_trasacao(conta, transacao)
    else:
        print("Transação invalidada devido a dados inconsistentes. Favor, Acione o gerente.")
        return

def sacar(clientes):
    cliente, conta = identificacao_cliente_conta(clientes)   
    valor = float(input("Digite o valor a ser depositado: "))
    transacao = Saque(valor)
    
    if cliente and conta and transacao:
        cliente.realizar_trasacao(conta, transacao)
    else:
        print("Transação invalidada devido a dados inconsistentes. Favor, Acione o gerente.")
        return
    
def extrato(clientes):
    cliente, conta = identificacao_cliente_conta(clientes)
    if cliente and conta:
        print("Extrato:".center(44, "-"))
        transacoes = conta.historico.transacoes
        if transacoes:
            data = 0
            extrato = ""
            for transacao in transacoes:
                if data != transacao.data:
                    data = transacao.data.strftime("%d/%m/%Y")
                    extrato += f"{transacao.data.strftime("%d/%m/%Y")}\n"
                else:
                    extrato += f"{transacao.data.strftime('%H:%M:%S')} - {transacao.tipo} - R$ {transacao.valor:,.2f}"
            print(extrato)
            print(f"Saldo:              R$ {conta.saldo:,.2f}")
        else:
            print("Não foram efetuadas transações até o momento nesta conta.")
        
    

def main():
    clientes = []
    contas = []

    while True:
        opcao = input(MENU)
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            extrato(clientes)
        elif opcao == 'a':
            pass
        elif opcao == 'c':
            pass
        elif opcao == 'x':
            break
        else:
            print("Opção inválida.")


def criar_usuario(clientes):
    cpf = input("Digite seu CPF: ").replace(".", "").replace("-", "")
    if consultar_usuario(cpf, clientes) != None:
        print("Cliente já cadastrado.")
        return None
    nome = input("Digite seu nome: ")
    data_nascimento = datetime.strptime(input("Digite sua data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado (sigla): ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    return clientes
    
def criar_conta_corrente(cpf, clientes, contas):
    if consultar_usuario(cpf, clientes) != None:    
        conta = len(contas) + 1
        agencia = "0001"
        saldo = 0
        extrato = {"extrato": {}}
        qtde_saques = 0
        contas.append({"conta": conta, "agencia": agencia, "saldo": saldo, "extrato": extrato, "qtde_saques": qtde_saques, "usuario": cpf})
    else:
        print("Cliente não encontrado.")
    return contas


def get_extrato(saldo, /, *, extrato):
    print("Extrato:".center(44, "-"))
    if len(extrato["extrato"]) < 1:
        print("Não foram realizadas operações até o momento")
    else:
        for data in extrato["extrato"]:
            print(data)
            for hora, transacao in extrato["extrato"][data].items():
                print(f"{hora} - {transacao['tipo_transacao']}             R$ {transacao['valor']:,.2f}")
    

while True:
    opção = input(MENU)
    if opção == 'd':
    elif opção == 's':
        usuario = selecionar_usuario(clientes)
        conta = selecionar_conta(contas, usuario.get('cpf'))
        if usuario != None and conta != None:
            if conta['qtde_saques'] < LIMITE_QUANT_SAQUES:
                conta['saldo'], conta['extrato'] = sacar(saldo=conta['saldo'], extrato=conta['extrato'])
            else:
                print("Limite diário de saques atingido.")
        else:
            print("Usuário ou conta não encontrados.")
    elif opção == 'e':
        usuario = selecionar_usuario(clientes)
        conta = selecionar_conta(contas, usuario.get('cpf'))
        if usuario != None and conta != None:
            get_extrato(conta['saldo'], extrato=conta['extrato'])
        else:
            print("Usuário ou conta não encontrados.")
    elif opção == 'c':
        clientes = criar_usuario(clientes)
    elif opção == 'a':
        cpf = input('digite o CPF do cliente:')
        contas = criar_conta_corrente(cpf, clientes, contas)
    elif opção == 'x':
        break
    else:
        print("Opção inválida.")