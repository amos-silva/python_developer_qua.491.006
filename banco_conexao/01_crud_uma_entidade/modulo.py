from datetime import datetime
import os


limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome da Pessoa: ").strip().title()
        email = input("Digite o Email: ").strip().lower()
        data_nasc = input("Digite a Data de Nascimento (dd/mm/aaaa): ").strip()

        data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y").date()
        nova_pessoa = Pessoa(nome=nome, email=email, data_nasc=data_nasc)

        session.add(nova_pessoa)    # faz a sessão no banco e envia o comando nova pessoa usando SQL automaticamente
        session.commit()            # Executa os comandos SQL dentro do banco

        print(f"\nA Pessoa: {nome}, foi cadastrada com Sucesso!")
    except Exception as e:
        print(f"Não foi possivel cadastrar !")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()    # lista tudo que tem na tabela Pessoa

        print("\n PESSOAS CADASTRADAS:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Email: {pessoa.email}")
            print(f"Data_Nasc: {pessoa.data_nasc.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}\n")
    except Exception as e:
        print(f"Não foi possivel Listar !")

def pesquisar_pessoas(session, Pessoa):
        
    print(f"{'-'*20}  Filtrar pessoas por campo  {'-'*20}")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-mail")
    print("4 - Data de Nasc.")
    print("5 - Retornar")

    campo = input("Informe o Campo a pesquisar: ").strip()

    limpar()

    match campo:
        case "1":
            valor = input("Digite o ID: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa.like(f"{valor}")).all()
        case "2":
            valor = input("Digite o Nome: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o E-mail: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a Data de Nasc. (dd/mm/aaaa) : ").strip()
            data_nasc = datetime.strptime(valor, "%d/%m/%Y").date()
            pessoas = session.query(Pessoa).filter(Pessoa.data_nasc == data_nasc).all()
        case "5":
            pass              

        case _:
            print("Campo inexistente !")

    limpar()

    print("\n RESULTADO DA PESQUISA:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de Nasc. : {pessoa.data_nasc.strftime("%d/%m/%Y")}\n")