from datetime import datetime

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
clientes = []
contas = []

qtde_saques = 0 #len(extrato["extrato"][get_data()]) if extrato["extrato"].get(get_data()) is not None else 0

def get_data():
    return datetime.today().strftime("%d/%m/%Y")

def get_hora():
    return datetime.today().strftime("%H:%M:%S")

def selecionar_usuario(clientes):
    cpf = input("Digite seu CPF: ").replace(".", "").replace("-", "")
    resposta = consultar_usuario(cpf, clientes)
    if resposta != None:
        return resposta
    else:
        print("Cliente não cadastrado.")
    return {}

def selecionar_conta(contas, cpf):
    contas_usuario = listar_contas(contas, cpf)
    if len(contas_usuario) > 0:
        for conta in contas_usuario:
            print(f"Conta: {conta['conta']} - Agência: {conta['agencia']}")
        conta = int(input("Digite o número da conta: "))
        for c in contas_usuario:
            if c["conta"] == conta:
                return c
    else:
        print("Cliente não possui contas.")
    return None


def listar_contas(contas, cpf):
    contas_usuario = []
    for conta in contas:
        if conta["usuario"] == cpf:
            contas_usuario.append(conta)
    return contas_usuario

def consultar_usuario(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None

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

def depositar(saldo, extrato,/):
    valor = float(input("Digite o valor a ser depositado: "))
    if valor > 0:
        saldo += valor
        extrato = set_extrato(extrato, "Depósito", valor)
    else:
        print("Valor inválido.")
    return saldo, extrato

def sacar(*, extrato, saldo):
    valor = float(input("Digite o valor a ser sacado: "))
    if 0 < valor <= LIMITE_SAQUE:
        if saldo >= valor:
            saldo -= valor
            extrato = set_extrato(extrato, "Saque", valor)
            qtde_saques += 1
        else:
            print("Saldo insuficiente.")
    else:
        print("Valor inválido ou fora do limite da conta.")
    return saldo, extrato

def set_extrato(extrato, tipo_transacao, valor):
    if extrato["extrato"].get(get_data()) != None:
        extrato["extrato"][get_data()][get_hora()] = {"tipo_transacao": tipo_transacao, "valor": valor}
    else:
        extrato["extrato"][get_data()] = {get_hora() :{"tipo_transacao": tipo_transacao, "valor": valor}}
    return extrato

def get_extrato(saldo, /, *, extrato):
    print("Extrato:".center(44, "-"))
    if len(extrato["extrato"]) < 1:
        print("Não foram realizadas operações até o momento")
    else:
        for data in extrato["extrato"]:
            print(data)
            for hora, transacao in extrato["extrato"][data].items():
                print(f"{hora} - {transacao['tipo_transacao']}             R$ {transacao['valor']:,.2f}")
    print(f"Saldo:              R$ {saldo:,.2f}")

while True:
    opção = input(MENU)
    if opção == 'd':
        usuario = selecionar_usuario(clientes)
        conta = selecionar_conta(contas, usuario.get('cpf'))
        if usuario != None and conta != None:
            conta['saldo'], conta['extrato'] = depositar(conta['saldo'], conta['extrato'])
        else:
            print("Usuário ou conta não encontrados.")
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