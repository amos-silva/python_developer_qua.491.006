#ABISTRAÇÃO = CLASSE QUE NÃO PODE SER INSTANCIADA PELO PROGRAMA
# IMPORTAR BIBLIOTECA ABC

from abc import ABC
from abc import abstractmethod

# classe Abstrata
class Conta(ABC):
    @abstractmethod
    def __init__(self, saldo):
        # atributo private       
        self.__saldo = saldo

    # METODOS GET e SET
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        

    # metodos de ação  -  que devo obrigar o programa a usar esses metodos
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, num_conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.agencia = agencia
        self.__num_conta = num_conta
        super().__init__(saldo)


    # METODOS GET
    @property
    def titular(self):
        return self.__titular
    @property
    def cpf(self):
        return self.__cpf
    @property
    def agencia(self):
        return self.__agencia
    @property
    def num_conta(self):
        return self.__num_conta
    

    # METODOS SET
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    @num_conta.setter
    def num_conta(self, num_conta):
        self.__num_conta = num_conta

    # METODOS DA INTERFACE -  os que defini acima , para serem obrigatórios de usar ( CONSULTAR, DEPOSITAR e SACAR )
    def consultar_dados(self):
        print("  ----- 🐍🐍🐍 DADOS DA CONTA 🐍🐍🐍 -----  \n")
        print(f"Titular da Conta: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Numero da Agencia: {self.agencia}")
        print(f"Numero da Conta: {self.num_conta}")
        print(f"Saldo em Conta: R$  {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    