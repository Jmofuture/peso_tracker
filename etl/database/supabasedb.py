"""Genera el cliente de Supabase"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client


def supabase_client():
    """
    Initializes and loads the Supabase client.

    This function loads the environment variables needed to connect to a
    Supabase database and creates a client instance for further interactions.

    Returns:
        Client: An instance of the Supabase client if the connection is successful.
        None: If there is an error connecting to Supabase.

    Raises:
        ValueError: If the provided URL or key is invalid or missing.
    """
    load_dotenv()

    supabase_url: str = os.getenv("SUPABASE_URL")
    supabase_key: str = os.getenv("SUPABASE_KEY")

    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        return supabase
    except ValueError as e:
        print(f"An error occurred while connecting to Supabase: {e}")
        return None


if __name__ == "__main__":
    client = supabase_client()
    if client:
        print("Successfully connected to Supabase")
    else:
        print("Failed to connect to Supabase")
