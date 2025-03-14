from historico import Historico

class Conta:
    def __init__(self, conta, cliente):
        self.agencia = "0001"
        self.conta = conta
        self.saldo = 0
        self.cliente = cliente
        self.historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def agencia(self):
        return self.agencia
    
    @property
    def conta(self):
        return self.conta
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def historico(self):
        return self.historico

    def depositar(self, valor):
        valida_valor = valor > 0
        if valida_valor:
            self.saldo += valor
            return True
        print("Valor inválido.")
        return False

    def sacar(self, valor):
        saldo = self.saldo
        saldo_suficiente = saldo >= valor
        if saldo_suficiente:
            self.saldo -= valor
            return True
        elif valor < 0:
            print("Valor inválido.")
        else:
            print("Saldo insuficiente.")
        return False

    def __str__(self):
        return f"Agência: {self.agencia} - Conta: {self.conta} - Saldo: {self.saldo}"