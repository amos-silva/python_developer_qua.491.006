import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    # Instanciar as classes
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # input do USUARIO
    print("Entre com os dados do USUÁRIO: \n")

    usuario.nome = input("informe o Nome: ").strip().title()
    usuario.cpf = input("informe o CPF: ").strip()
    usuario.telefone = input("informe o Telefone: ").strip().title()
    usuario.endereco = input("informe o Endereço: ").strip().title()

    limpar()

    # input da EMPRESA
    print("Entre com os dados da EMPRESA: \n")

    empresa.nome_fantasia = input("informe o Nome Fantasia: ").strip().title()
    empresa.cnpj = input("informe o CNPJ: ").strip()
    empresa.telefone = input("informe o Telefone: ").strip().title()
    empresa.endereco = input("informe o Endereço: ").strip().title()

    # output
    limpar()
    print("DADOS do USUARIO:")
    usuario.exibir_dados()

    print("\nDADOS da EMPRESA:")
    empresa.exibir_dados()
