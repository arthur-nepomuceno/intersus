from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URL do banco de dados da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria a fábrica de sessões do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos ORM (usada em models.py)
Base = declarative_base()
