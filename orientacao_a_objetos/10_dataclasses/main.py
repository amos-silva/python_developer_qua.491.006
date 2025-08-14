import Pessoa
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa.Pessoa(nome="", email="", cpf="", idade="0", altura="0.0")

    usuario.nome = input("Informe seu Nome: ").title().strip()
    usuario.email = input("Informe seu Email: ").lower().strip()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua Idade: "))
    usuario.altura = float(input("Informe sua Altura: ").replace(",","."))

    limpar()

    print(usuario)


if __name__ == "__main__":
    main()