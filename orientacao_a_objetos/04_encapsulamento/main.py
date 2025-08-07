import os
import classes as c

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # INSTANCIA OU OBJETO
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(fantasia="", cnpj="", telefone="", endereco="")


    #SETAR OS VALORES
    print("INSIRA OS DADOS DO USUARIO:\n")

    usuario.nome = input("Informe o NOME: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.telefone = input("Informe o TELEFONE: ").strip().title()
    usuario.endereco = input("Informe o ENDEREÇO: ").strip().title()

    limpar()

    #SETAR OS VALORES
    print("INSIRA OS DADOS DA EMPRESA:\n")

    empresa.fantasia = input("Informe o nome FANTASIA: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.telefone = input("Informe o TELEFONE: ").strip().title()
    empresa.endereco = input("Informe o ENDEREÇO: ").strip().title()

    limpar()

    # CHAMAR OS METODOS GET - APRESENTAÇÃO
    print("DADOS DO USUARIO:")
    print(f"Nome do usuario: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Endereço: {usuario.endereco}")

    print("\nDADOS DA EMPRESA:")
    print(f"Nome da Empresa: {empresa.fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Telefone: {empresa.telefone}")
    print(f"Endereço: {empresa.endereco}")

if __name__ == "__main__":
    main()
