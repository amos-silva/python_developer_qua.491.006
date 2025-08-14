import PessoaFisica
import PessoaJuridica
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica.PessoaFisica(nome="", cpf="", idade="0", email="", telefone="", endereco="")
    empresa = PessoaJuridica.PessoaJuridica(razao_social="", fantasia="", cnpj="", email="", telefone="", endereco="")

    print("----- INFORME OS DADOS DA PESSOA -----")
    usuario.nome = input("Informe seu Nome: ").title().strip()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua Idade: "))
    usuario.email = input("Informe seu Email: ").lower().strip()
    usuario.telefone = input("Informe seu Telefone: ").strip()
    usuario.endereco = input("Informe seu Endereço: ").title().strip()
    
    print("----- INFORME OS DADOS DA EMPRESA -----")
    empresa.razao_social = input("Informe a Razão Social da Empresa: ").title().strip()
    empresa.fantasia= input("Informe o Nome Fantasia: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ: ").title().strip()
    empresa.email = input("Informe Email: ").lower().strip()
    empresa.telefone = input("Informe Telefone: ").strip()
    empresa.endereco = input("Informe o Endereço: ").title().strip()

    limpar()

    print(usuario)

    print(empresa)

if __name__ == "__main__":
    main()