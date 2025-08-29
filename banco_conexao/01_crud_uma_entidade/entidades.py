
# sql injection - ATAQUE RACKER ao Banco
# prepared statement - metodo de consultar o banco de forma INDIRETA - Camada de proteção contra ataques ao Banco

# engine para o MySQL , e tbm instalar o Driver (MySQL connector)
# engine = create_engine("mysql+msqlconnector://senha:usuario@endereço do servidor:porta/nome do banco")
      
#importar biblioteca sqlalchemy
from sqlalchemy import Column, Integer, String, Date        # faz a conexão do python com o Banco

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
