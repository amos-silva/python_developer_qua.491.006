import os

class Conta:
    # Construtor / Método
    def __init__(self, titular, cpf, agencia, num_conta, saldo):
        # ATRIBUTOS
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    # Construtor / Método
    def apresentar(self):
        return f"NOME: {self.titular}, CPF: {self.cpf}, AGENCIA: {self.agencia}, CONTA: {self.num_conta}, SALDO: {self.saldo} "
    