
# sql injection - ATAQUE RACKER ao Banco
# prepared statement - metodo de consultar o banco de forma INDIRETA - Camada de proteção contra ataques ao Banco
      
#importar biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date             # faz a conexão do python com o Banco
from sqlalchemy.orm import declarative_base                                     # recurso que permite gerar uma classe e que assim gera as tabelas do banco

try:
    # engine para o MySQL , e tbm instalar o Driver (MySQL connector)
    # engine = create_engine("mysql+msqlconnector://senha:usuario@endereço do servidor:porta/nome do banco")

    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()   # Objeto que representa Classe nativa do banco SQLite

    class Pessoa(Base):
        __tablename__ = "pessoa"

        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        data_nasc = Column(Date, nullable=False)
    
    Base.metadata.create_all(engine)    # comando para criar a tabela no banco

except Exception as e:
    print(f"Erro ao conectar ao Banco. {e}")
