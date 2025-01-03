"""Obtener los datos desde la URL"""

import os
import requests
import validators

from dotenv import load_dotenv


def load_url_from_env() -> str:
    """
    Load a URL from environment variables.

    Returns:
        str: The URL loaded from the environment variables.

    Raises:
        ValueError: If 'URL_DATAFRAME' is not found or if the provided URL is invalid.
    """
    load_dotenv()
    url: str = os.getenv("URL_DATAFRAME")
    if not url:
        raise ValueError("'URL_DATAFRAME' was not found in the environment variables.")
    if not validators.url(url):
        raise ValueError(f"The provided URL is invalid: {url}")
    return url


def fetch_data_from_url(url: str) -> bytes:
    """
    Fetch data from a given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        bytes: The data fetched from the URL.

    Raises:
        requests.exceptions.HTTPError: If there is an HTTP error.
        requests.exceptions.ConnectionError: If there is a connection error.
        requests.exceptions.Timeout: If the request times out.
    """
    try:
        response: requests.Response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        raise
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
        raise
    except requests.exceptions.Timeout as e:
        print(f"Timeout error: {e}")
        raise


def extract_data_from_url() -> bytes:
    """
    Extract data from the URL without saving it to a file.

    Returns:
        bytes: The downloaded data.

    Raises:
        Exception: If there is an error during the process.
    """
    try:
        url: str = load_url_from_env()
        file_data: bytes = fetch_data_from_url(url)
        print("Data downloaded successfully.")
        return file_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    data = extract_data_from_url()
    if data:
        print(f"Data extracted from the URL: {len(data)} bytes")
    else:
        print("Failed to extract data.")
