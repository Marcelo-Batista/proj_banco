from datetime import date, time

def get_data():
    return date.now().strftime("%d/%m/%Y")


def get_hora():
    return time.now().strftime("%H:%M:%S")

def depositar():
    valor = float(input("Digite o valor a ser depositado: "))
    if valor > 0:
        saldo += valor
        set_extrato("deposito", valor)
        #extrato += f"Depósito:           R$ {valor:,.2f}\n"
    else:
        print("Valor inválido.")

def sacar():
    if not extrato["extrato"].get(get_data) or extrato["extrato"][get_data].count() <= LIMITE_QUANT_SAQUES:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > 0 and valor <= LIMITE_SAQUE and valor <= saldo:
            saldo -= valor
            set_extrato("saque", valor)
            #extrato += f"Saque:             -R$ {valor:,.2f}\n"
            #quantidade_saques += 1
        else:
            print("Valor inválido.")
    else:
        print("Limite de saques excedido.")

def set_extrato(tipo_trasacao, valor):
    if extrato["extrato"].get(get_data()):
        extrato["extrato"][get_data()].append({get_time():{"tipo_transacao": tipo_trasacao, "valor": valor}})
    else:
        extrato["extrato"].append({get_data: {get_time():{"tipo_transacao": tipo_trasacao, "valor": valor}}})
    

def get_extrato():
    print("Extrato:".center(44, "-"))
    print("Não foram realizadas operações até o momento" if not extrato else extrato)
    print(f"Saldo:              R$ {saldo:,.2f}")

menu = '''

[d] Depositar
[w] Sacar
[s] Extrato
[q] Sair

'''

saldo = 0
extrato = dict.fromkeys("extrato", "")
quantidade_saques = 0
LIMITE_SAQUE = 500
LIMITE_QUANT_SAQUES = 10

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