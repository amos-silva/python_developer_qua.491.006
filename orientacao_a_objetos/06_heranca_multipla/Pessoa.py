class Pessoa:
    def __init__(self, nome, cpf, email, profissao, telefone, endereco, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__profissao = profissao
        self.__telefone = telefone
        self.__endereco = endereco
        self.__salario = salario
    
    # METODO GET
    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def email(self):
        return self.__email
    @property
    def profissao(self):
        return self.__profissao
    @property
    def telefone(self):
        return self.__telefone
    @property
    def endereco(self):
        return self.__endereco
    @property
    def salario(self):
        return self.__salario
    
    
    # METODO SET
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    @email.setter
    def email(self, email):
        self.__email = email
    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    @salario.setter
    def salario(self, salario):
        self.__salario = salario


    def exibir_dados(self):
        print(f"DADOS da CONTA \n")     
        print(f"Nome do Titular: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"EMAIL: {self.email}")
        print(f"Profissão: {self.profissao}")
        print(f"TELEFONE: {self.telefone}")
        print(f"ENDEREÇO: {self.salario}")