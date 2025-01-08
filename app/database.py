from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import Config

DATABASE_URL = "postgresql://<username>:<password>@<rds-endpoint>/<database>"

engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

