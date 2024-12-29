"""Obtener los datos desde la URL"""

import os
import requests
import validators

from dotenv import load_dotenv


def load_url_from_env() -> str:
    """Load URL from environment variables."""
    load_dotenv()
    url: str = os.getenv("URL_DATAFRAME")
    if not url:
        raise ValueError("No se encontró 'URL_DATAFRAME' en las variables de entorno.")
    if not validators.url(url):
        raise ValueError(f"La URL proporcionada no es válida: {url}")
    return url


def fetch_data_from_url(url: str) -> bytes:
    """Fetch data from a given URL."""
    try:
        response: requests.Response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
        raise
    except requests.exceptions.ConnectionError as e:
        print(f"Error de conexión: {e}")
        raise
    except requests.exceptions.Timeout as e:
        print(f"Tiempo de espera agotado: {e}")
        raise


def extract_data_from_url() -> bytes:
    """Extract data from the URL without saving it to a file."""
    try:
        # Obtener la URL desde las variables de entorno
        url: str = load_url_from_env()

        # Descargar los datos desde la URL
        file_data: bytes = fetch_data_from_url(url)

        # Aquí simplemente devolvemos los datos descargados sin guardarlos
        print("Datos descargados con éxito.")
        return file_data

    except Exception as e:
        print(f"Se produjo un error: {e}")
        return None


if __name__ == "__main__":
    data = extract_data_from_url()
    if data:
        print(f"Datos extraídos de la URL: {len(data)} bytes")
    else:
        print("No se pudieron extraer los datos.")
