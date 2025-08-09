import Pessoa as p
import Conta as c

class ContaCorrente(p.Pessoa, c.Conta):
    def __init__(self, nome, cpf, email, profissao, telefone, endereco, salario, agencia, num_conta, saldo):
        p.Pessoa.__init__(self, nome, cpf, email, profissao, telefone, endereco, salario)
        c.Conta.__init__(self, agencia, num_conta, saldo)


    def exibir_dados(self):
        p.Pessoa.exibir_dados(self)
        c.Conta.exibir_dados(self)
        