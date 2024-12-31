"""Coneccion a Supabase"""

import os
from sqlmodel import create_engine, Session
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL_C = os.getenv("SUPABASE_URL_C")
SUPABASE_PORT = os.getenv("SUPABASE_PORT")
SUPABASE_USER = os.getenv("SUPABASE_USER")
SUPABASE_DATABASE = os.getenv("SUPABASE_DATABASE")
SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")


DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username=SUPABASE_USER,
    password=SUPABASE_PASSWORD,
    host=SUPABASE_URL_C,
    port=SUPABASE_PORT,
    database=SUPABASE_DATABASE,
)


engine = create_engine(DATABASE_URL)


def get_session():
    """Proporciona una sesión para interactuar con la base de datos"""
    try:
        with Session(engine) as session:
            yield session
    except ImportError as ei:
        print(f"Hubo un error: {ei}")


if __name__ == "__main__":
    print(get_session())
