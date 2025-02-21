from datetime import datetime

def depositar():
    valor = float(input("Digite o valor a ser depositado: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:           R$ {valor:,.2f}\n"
    else:
        print("Valor inválido.")

def sacar():
    if quantidade_saques < LIMITE_QUANT_SAQUES:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > 0 and valor <= LIMITE_SAQUE and valor <= saldo:
            saldo -= valor
            extrato += f"Saque:              R$ {valor:,.2f}\n"
            quantidade_saques += 1
        else:
            print("Valor inválido.")
    else:
        print("Limite de saques excedido.")

def extrato():
    print("Extrato:".center(44, "-"))
    print("Não foram realizadas operações até o momento" if not extrato else extrato)
    print(f"Saldo:              R$ {saldo:,.2f}")

menu = '''

[d] Depositar
[w] Sacar
[s] Extrato
[q] Sair

'''
data_hoje = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
saldo = 0
extrato = ""
quantidade_saques = 0
LIMITE_SAQUE = 500
LIMITE_QUANT_SAQUES = 3

while True:
    opção = input(menu)
    if opção == 'd':
        depositar()  
    elif opção == 'w':
        sacar()
    elif opção == 's': 
        extrato()
    elif opção == 'q':
        break
    else:
        print("Opção inválida.")