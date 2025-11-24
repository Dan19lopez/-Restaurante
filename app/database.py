from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./restaurante.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Si en algún caso necesitas usar la sesión con with o yield (FastAPI):
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()