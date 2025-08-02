# classe
class Pessoa:
    # atributos
    nome = "Amós"
    idade = 39
    tel =   "(61)98999-7777"
    cpf = "123.123.123-11"
    email = "amos@amos.com"

    # Métodos " Funções ou Ações"
    def apresentar(self):
        print(f"Olá, meu nome é: {self.nome}, tenho {self.idade}, meu Telefone é: {self.tel}, meu CPF é: {self.cpf}, meu email: {self.email} ")

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    #instanciar classe - CRIAR
    usuario = Pessoa()

    # Objeto se apresenta
    usuario.apresentar()