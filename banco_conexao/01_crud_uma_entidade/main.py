
# sql injection - ATAQUE RACKER ao Banco
# prepared statement - metodo de consultar o banco de forma INDIRETA - Camada de proteção contra ataques ao Banco

# engine para o MySQL , e tbm instalar o Driver (MySQL connector)
# engine = create_engine("mysql+msqlconnector://senha:usuario@endereço do servidor:porta/nome do banco")
      
#importar biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date        # faz a conexão do python com o Banco
from sqlalchemy.orm import declarative_base, sessionmaker                  # recurso que permite gerar uma classe e que assim gera as tabelas do banco
from datetime import datetime
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def criar_tab_pessoa(engine, Base):
    try:
        
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nasc = Column(Date, nullable=False)
        
        Base.metadata.create_all(engine)    # comando para criar a tabela no banco

        return Pessoa

    except Exception as e:
        print(f"Erro ao conectar ao Banco. {e}")

def cadastrar_pessoa(session, Pessoa):
    nome = input("Digite o nome da Pessoa: ").strip().title()
    email = input("Digite o Email: ").strip().lower()
    data_nasc = input("Digite a Data de Nascimento (dd/mm/aaaa): ").strip()

    data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y").date()
    nova_pessoa = Pessoa(nome=nome, email=email, data_nasc=data_nasc)

    session.add(nova_pessoa)    # faz a sessão no banco e envia o comando nova pessoa usando SQL automaticamente
    session.commit()            # Executa os comandos SQL dentro do banco

    print(f"\nA Pessoa: {nome}, foi cadastrada com Sucesso!")

def listar_pessoas(session, Pessoa):
    pessoas = session.query(Pessoa).all()    # lista tudo que tem na tabela Pessoa

    print("\n PESSOAS CADASTRADAS:\n")
    for pessoa in pessoas:
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"Email: {pessoa.email}")
        print(f"Data_Nasc: {pessoa.data_nasc.strftime("%d/%m/%Y")}")
        print(f"{'-'*40}\n")


def main():

    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()   # Objeto que representa Classe nativa do banco SQLite

    Pessoa = criar_tab_pessoa(engine, Base)
    session = sessionmaker(bind=engine)
    session = session()

    limpar()
    while True:
        print(f"{'-'*20} 🐍 CRUD DA SERPENTE 🐍 {'-'*20}")
        print("1 - Cadastrar nova Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Alterar Dados de uma Pessoa")
        print("4 - Excluir uma Pessoa")
        print("5 - SAIR")

        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                listar_pessoas(session, Pessoa)
                continue

            case "3":
                pass

            case "4":
                pass

            case "5":
                print("Você SAIU !")
                break

            case _:
                print("Opção invalida")
                continue
                
    session.close()

if __name__ == "__main__":
    main()