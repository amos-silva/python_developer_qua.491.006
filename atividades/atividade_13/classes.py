import json

class Conta:
    # Construtor
    def __init__(self, titular, cpf, agencia, num_conta, saldo):
        # ATRIBUTOS
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo


    # METODOS

    def consultar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agencia: {self.agencia}")
        print(f"Conta: {self.num_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")


    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def extrato(self):
        dados = {
            "Titular": self.titular,
            "CPF": self.cpf,
            "Agencia": self.agencia,
            "Conta": self.num_conta,
            "Saldo": self.saldo
        }


        # Criar Arquivo Json para salvar os dados
        with open("conta.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
