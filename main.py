from datetime import datetime

LIMITE_SAQUE = 500
LIMITE_QUANT_TRANSACOES = 10
MENU = '''

[d] Depositar
[w] Sacar
[s] Extrato
[q] Sair

'''

saldo = 0
extrato = {"extrato": {}}


def get_data():
    return datetime.today().strftime("%d/%m/%Y")

def get_hora():
    return datetime.today().strftime("%H:%M:%S")

def depositar(saldo, extrato):
    if not extrato["extrato"].get(get_data()) or len(extrato["extrato"][get_data()]) < LIMITE_QUANT_TRANSACOES:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato = set_extrato(extrato, "Depósito", valor)
            
        else:
            print("Valor inválido.")
    else:
        print("Limite de transações atingido.")
    return saldo, extrato

def sacar(saldo, extrato):
    if not extrato["extrato"].get(get_data()) or len(extrato["extrato"][get_data()]) <= LIMITE_QUANT_TRANSACOES:
        valor = float(input("Digite o valor a ser sacado: "))
        if 0 < valor <= LIMITE_SAQUE and valor <= saldo:
            saldo -= valor
            extrato = set_extrato(extrato, "Saque   ", valor)
        else:
            print("Valor inválido.")
    else:
        print("Limite de transações atingido.")
    return saldo, extrato

def set_extrato(extrato, tipo_transacao, valor):
    if extrato["extrato"].get(get_data()) != None:
        extrato["extrato"][get_data()][get_hora()] = {"tipo_transacao": tipo_transacao, "valor": valor}
    else:
        extrato["extrato"][get_data()] = {get_hora() :{"tipo_transacao": tipo_transacao, "valor": valor}}
    return extrato

def get_extrato(extrato):
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
        saldo, extrato = depositar(saldo, extrato)
    elif opção == 'w':
        saldo, extrato = sacar(saldo, extrato)
    elif opção == 's':
        get_extrato(extrato)
    elif opção == 'q':
        break
    else:
        print("Opção inválida.")