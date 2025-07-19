from db import engine, Base
from models import Patient

# Cria todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso.")
                                                                                                        