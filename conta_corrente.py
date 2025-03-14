from conta import Conta
from saque import Saque

class Conta_corrente(Conta):
    def __init__(self, conta, cliente, qtde_saques=3, limite=500):
        super().__init__(conta, cliente)
        self.qtde_saques = qtde_saques
        self.limite = limite
    
    def sacar(self, valor):
        saques_realizados = len(
            [transacao for transacao in self.historico.transacoes if transacao.tipo == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_qtde_saques = saques_realizados >= self.qtde_saques

        if excedeu_limite:
            print("Valor excede o limite de saque.")
        elif excedeu_qtde_saques:
            print("Quantidade de saques excedida.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"Agência: {self.agencia}\nC/C: {self.conta}\nCliente: {self.cliente.nome}"
            
        
