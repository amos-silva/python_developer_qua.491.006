from datetime import datetime
import pandas
from sqlalchemy import create_engine
import os


limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome da Pessoa: ").strip().title()
        email = input("Digite o Email: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"{email}")).all()

        if email in [pessoa.email for pessoa in pessoas]:
            print("E-mail já cadastrado !")
        else:
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
    else:
        print("Nenhuma pessoa encontrada.")


def alterar_dados(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email = ""
    nova_data = ""
    try:
        print("\nPESQUISAR POR ?")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Retornar")
    
        opcao = input("Informe o Campo a pesquisar: ").strip()
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()            
            case "2":
                email = input("Informe o email: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""          
            case _:
                print("Campo inexistente !")

        if pessoa:
            while True:
                print("DADOS DA PESSOA:\n")
                print(f"ID: {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data_Nasc.: {pessoa.data_nasc.strftime("%d/%m/%Y")}")
                print(f"4 - Finalizar")

                campo = input("Informe o que deseja alterar: ").strip()
                limpar()

                match campo:
                    case "1":
                        novo_nome = input("Novo Nome: ").strip().title()
                        print(f"Novo nome cadastrado: {novo_nome}")
                        continue
                    case "2":
                        novo_email = input("novo E-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == (f"{novo_email}")).all()
                        if email in [pessoa.email for pessoa in pessoas]:
                            print("E-mail já cadastrado - ERRO !")
                        else:
                            print(f"Novo E-mail cadastrado: {novo_email}")
                        continue
                    case "3":
                        nova_data = input("Nova Data de Nasc. (dd/mm/aaaa):  ").strip()
                        print(f"Nova data cadastrada: {nova_data}")
                        continue
                    
                    case "4":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email !="" else pessoa.email
                        nova_data = datetime.strptime(nova_data, "%d/%m/%Y").date() if nova_data != "" else pessoa.data_nasc
                        break
                    case _:
                        print("Campo inexistente.")
                        continue    
            
            # inserir as alterações no Banco
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.data_nasc = nova_data

            session.commit()

            print("Alteração realizada com sucesso !")

        else:
            print("Pessoa não encontrada.")

    except Exception as e:
        print(f"Não foi possivel alterar. {e}")

def excluir_pessoa(session, Pessoa):
    id_pessoa = ""
    email = ""
    pessoa = ""

    print("Escolha o campo que deseja Pesquisar a pessoa, para excluir")
    print("1 - ID")
    print("2 - E-mail")
    print("3 - Desistir")
    
    opcao = input("Informe o campo que deseja pesquisar: ").strip()

    match opcao:
        case "1":
            id_pessoa = input("\nInforme o ID a ser excluido: ").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
        case "2":
            email = input("Informe o E-mail a ser excluido: ").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first()
            
        case "3":
            return  ""
        case _:
            print("Opção inválida !")
    limpar()
    if pessoa:
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"E-mail: {pessoa.email}")
        print(f"Data_Nasc: {pessoa.data_nasc.strftime("%d/%m/%Y")}")

        
        print("\nTEM CERTEZA QUE DESEJA EXCLUIR ?")
        print("1 - SIM")
        print("2 - NÃO")
        excluir = input(" EXCLUIR ? ").strip()

        match excluir:
            case "1":
                session.delete(pessoa)
                session.commit()
                print(f"Pessoa excluida com Sucesso ! ")
            case "2":
                pass
            case _:
                print("Opção invalida !")
    else:
        print("pessoa não encontrada ")
    

# TODO: criar função que exporte os dados para arquivo .csv
def exportar_dados(session, Pessoa):
    sql_query = "SELECT * from  Pessoa"

    df= pandas.read_sql_query(sql_query, session.bind)
    df.to_csv('dados_exportados.csv', index=False)

    print("Dados exportados com sucesso !")