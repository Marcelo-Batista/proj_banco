from historico import Historico

class Conta:
    def __init__(self, conta, cliente):
        self._agencia = "0001"
        self._conta = conta
        self._saldo = 0
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        valida_valor = valor > 0
        if valida_valor:
            self._saldo += valor
            return True
        print("Valor inválido.")
        return False

    def sacar(self, valor):
        saldo = self._saldo
        saldo_suficiente = saldo >= valor
        if saldo_suficiente:
            self._saldo -= valor
            return True
        elif valor < 0:
            print("Valor inválido.")
        else:
            print("Saldo insuficiente.")
        return False

    def __str__(self):
        return f"Agência: {self.agencia} - Conta: {self.conta} - Saldo: {self.saldo}"