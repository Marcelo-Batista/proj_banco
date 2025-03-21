from datetime import datetime
from conta_corrente import Conta_corrente
from deposito import Deposito
from pessoa_fisica import Pessoa_fisica
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
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
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
    numero = int(input("Digite o número da conta: "))
    conta = filtrar_contas(contas, numero)
    return conta

def identificacao_cliente_conta(clientes):
    cliente = selecionar_cliente(clientes)
    if not cliente:
        print("Cliente não encontrado.")
        return None, None
    
    conta = selecionar_conta(cliente.contas)
    if not conta:
        print("Conta não encontrada.")
        return cliente, None
    
    return cliente, conta

def depositar(clientes):
    cliente, conta = identificacao_cliente_conta(clientes)   
    
    if cliente and conta:
        valor = float(input("Digite o valor a ser depositado: "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)
    else:
        print("Transação invalidada devido a dados inconsistentes. Favor, Acione o gerente.")

def sacar(clientes):
    cliente, conta = identificacao_cliente_conta(clientes)   
    
    if cliente and conta:
        valor = float(input("Digite o valor a ser sacado: "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)
    else:
        print("Transação invalidada devido a dados inconsistentes. Favor, Acione o gerente.")
    
def extrato(clientes):
    cliente, conta = identificacao_cliente_conta(clientes)
    if cliente and conta:
        print("Extrato:".center(44, "-"))
        transacoes = conta.historico.transacoes
        if transacoes:
            data = 0
            extrato = ""
            for registro in transacoes:
                data_hora = registro["data"].split(" ")
                if data != data_hora[0]:
                    data = data_hora[0]
                    extrato += f"{data}\n{data_hora[1]} - {registro["tipo"]}" + f"R$ {registro["valor"]:,.2f}\n".rjust(25, " ")
                else:
                    extrato += f"{data_hora[1]} - {registro["tipo"]}" + f"R$ {registro["valor"]:,.2f}\n".rjust(25, " ")
            print(extrato)
            print(f"Saldo:   ", f"R$ {conta.saldo:,.2f}".rjust(30, " "))
        else:
            print("Não foram efetuadas transações até o momento nesta conta.")

def abrir_conta(contas, clientes):
    cliente = selecionar_cliente(clientes)
    if not cliente:
        print("Cliente não encontrado.")
        return
    
    conta = Conta_corrente.nova_conta(len(contas) + 1, cliente)
    contas.append(conta)
    print(f"Conta {conta.conta} aberta com sucesso.")
    cliente.adicionar_conta(conta)

def criar_usuario(clientes):
    cpf = input("Digite o CPF: ")
    cliente = filtrar_clientes(clientes, cpf)
    if cliente:
        print("Cliente já cadastrado.")
        return clientes
    
    nome = input("Digite o nome: ")
    data_nascimento = datetime.strptime(input("Digite a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
    endereco = input("Digite o endereço seguindo o formato (logradouro, numero - bairro - cidade/sigla do estado): ")
    cliente = Pessoa_fisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")

def main():
    clientes, contas = [], []

    while True:

        opcao = input(MENU)
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            extrato(clientes)
        elif opcao == 'a':
            abrir_conta(contas, clientes)
        elif opcao == 'c':
            criar_usuario(clientes)
        elif opcao == 'x':
            break
        else:
            print("Opção inválida.")


main()