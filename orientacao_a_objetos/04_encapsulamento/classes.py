# ENCAPSULAMENTOS
# public=  self.telefone = telefone
# protected= self._telefone = telefone
# private=  self.__telefone = telefone

# superclasse
class Pessoa:
    def __init__(self, telefone, endereco):
        self.__telefone = telefone  # private
        self.__endereco = endereco   # private


    # metodo de acesso - GET
    @property
    def telefone(self):
        return self.__telefone

    # metodo de acesso - SET
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone


    # metodo de acesso - GET
    @property
    def endereco(self):
        return self.__endereco

    # metodo de acesso - SET
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(telefone, endereco)

    
    # metodo de acesso - GET
    @property
    def nome(self):
        return self.__nome

    # metodo de acesso - SET
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # metodo de acesso - GET
    @property
    def cpf(self):
        return self.__cpf

    # metodo de acesso - SET
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__(self, fantasia, cnpj ,telefone, endereco):
        self.__fantasia = fantasia
        self.__cnpj = cnpj
        super().__init__(telefone, endereco)

    
    # metodo de acesso - GET
    @property
    def fantasia(self):
        return self.__fantasia
    
    @property
    def cnpj(self):
        return self.__cnpj
    

    # metodo de acesso - SET
    @fantasia.setter
    def fantasia(self, fantasia):
        self.__fantasia = fantasia

    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj
