from cliente import Cliente

class Pessoa_fisica(Cliente):
    def __init__(self, _nome, _cpf,_data_nascimento, _endereco):
        super().__init__(_endereco)
        self.nome = _nome
        self.cpf = _cpf
        self.data_nascimento = _data_nascimento