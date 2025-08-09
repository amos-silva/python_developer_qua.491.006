import InterfaceConta as i

class Conta(i.IConta):
    def __init__(self, agencia, num_conta, saldo):
        self.__agencia = agencia
        self.__num_conta = num_conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia
    @property
    def num_conta(self):
        return self.__num_conta
    @property
    def saldo(self):
        return self.__saldo
    

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    @num_conta.setter
    def num_conta(self, num_conta):
        self.__num_conta = num_conta
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # metodos da interface - QUE FORAM IMPORTADOS
    def exibir_dados(self):
        print(f"Agencia: {self.agencia}")
        print(f"Conta: {self.num_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    def depositar(self,valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo