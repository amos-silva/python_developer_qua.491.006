
# sql injection - ATAQUE RACKER ao Banco
# prepared statement - metodo de consultar o banco de forma INDIRETA - Camada de proteção contra ataques ao Banco
# engine para o MySQL , e tbm instalar o Driver (MySQL connector)
# engine = create_engine("mysql+msqlconnector://senha:usuario@endereço do servidor:porta/nome do banco")
      
#importar biblioteca sqlalchemy
from sqlalchemy import create_engine                                       # faz a conexão do python com o Banco
from sqlalchemy.orm import declarative_base, sessionmaker                  # recurso que permite gerar uma classe e que assim gera as tabelas do banco
import entidades as ent
import modulo as mod

def main():

    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()   # Objeto que representa Classe nativa do banco SQLite
   

    Pessoa = ent.criar_tab_pessoa(engine, Base)
    session = sessionmaker(bind=engine)
    session = session()

    mod.limpar()
    while True:
        print(f"{'-'*20} 🐍 CRUD DA SERPENTE 🐍 {'-'*20}")
        print("1 - Cadastrar nova Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Pesquisar Pessoas")
        print("4 - Alterar Dados de uma Pessoa")
        print("5 - Excluir uma Pessoa")
        print("6 - Exportar Dados")
        print("7 - SAIR")

        opcao = input("\nInforme a opção desejada: ").strip()

        match opcao:
            case "1":
                mod.cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                mod.listar_pessoas(session, Pessoa)
                continue
            case "3":
                mod.pesquisar_pessoas(session, Pessoa)
                continue
            case "4":
                mod.alterar_dados(session, Pessoa)
            case "5":
                mod.excluir_pessoa(session, Pessoa)
                continue
            case "6":
                mod.exportar_dados(session, Pessoa)
                continue
            case "7":
                print("Você SAIU !")
                break

            case _:
                print("Opção invalida")
                continue
                
    session.close()

if __name__ == "__main__":
    main()