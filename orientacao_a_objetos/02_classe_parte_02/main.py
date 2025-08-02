# classe
class Pessoa:
    # Construtor / Método
    def __init__(self, nome, idade, telefone, cpf, email):
        # ATRIBUTOS
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    # Construtor / Método
    def apresentar(self):
        return f"Olá, menu nome é: {self.nome}, minha idade é: {self.idade}, meu telefone é: {self.telefone}, meu cpf: {self.cpf}, e meu email: {self.email} "
    
# ALGORITIMO PRINCIPAL

if __name__ == "__main__":
    usuario = Pessoa(
        nome="",
        idade=0,
        telefone="",
        cpf="",
        email=""
    )

    # INPUT
    try:
        usuario.nome = input("Informe seu Nome: ").strip().title()
        usuario.idade = int(input("Informe sua Idade: "))
        usuario.telefone = input("Informe seu Telefone: ").strip()
        usuario.cpf = input("Informe seu CPF: ").strip()
        usuario.email = input("Informe seu Email: ").strip().lower()

        # CHAMAR O METODO
        print(usuario.apresentar())
    
    except Exception as e:
        print("ERRO ao criar Objeto. {e}")