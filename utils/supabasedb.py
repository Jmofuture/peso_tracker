"""Genera el cliente de Supabase"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client


def supabase_client():
    """
    Carga el cliente de Supabase.
    """
    load_dotenv()

    supabase_url: str = os.getenv("SUPABASE_URL")
    supabase_key: str = os.getenv("SUPABASE_KEY")

    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        return supabase
    except ValueError as e:
        print(f"Hubo un error al conectar con Supabase: {e}")
        return None


if __name__ == "__main__":
    client = supabase_client()
    if client:
        print("Conexión exitosa a Supabase")
    else:
        print("No se pudo conectar a Supabase")
