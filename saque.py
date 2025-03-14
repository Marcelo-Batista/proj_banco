from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.transacoes.append(self)
    