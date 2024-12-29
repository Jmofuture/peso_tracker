"""Procesar y limpiar el DF obtenido desde la URL"""

from io import BytesIO
import pandas as pd


def bytes_to_dataframe(data: bytes) -> pd.DataFrame:
    """Convert bytes data (Excel) to a DataFrame."""
    try:
        excel_data = BytesIO(data)
        df = pd.read_excel(excel_data)

        return df
    except ValueError as e:
        print(f"Error al convertir los bytes en DataFrame: {e}")
        raise


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform the dataframe."""

    column_mapping = {
        "Fecha": "date",
        "Dólar.USA.Compra": "usd_buy",
        "Dólar.USA.Venta": "usd_sell",
        "Dólar.eBROU.Compra": "ebrou_usd_buy",
        "Dólar.eBROU.Venta": "ebrou_usd_sell",
        "Euro.Compra": "eur_buy",
        "Euro.Venta": "eur_sell",
        "Peso.Argentino.Compra": "ars_buy",
        "Peso.Argentino.Venta": "ars_sell",
        "Real.Compra": "brl_buy",
        "Real.Venta": "brl_sell",
    }
    try:
        df_renamed = df.rename(columns=column_mapping)

        return df_renamed
    except ValueError as e:
        print(f"Error al limpiar el dataframe: {e}")
    except KeyError as e:
        print(f"Error al limpiar el dataframe: {e}")


def remove_columns(df: pd.DataFrame, columns_to_remove: list) -> pd.DataFrame:
    """Elimina las columnas especificadas del DataFrame."""
    try:
        df = df.drop(columns=columns_to_remove)
        return df
    except KeyError as e:
        print(f"Las columnas a eliminar no se encuentran en el DataFrame: {e}")
        raise
    except ValueError as e:
        print(f"Las columnas a eliminar no se encuentran en el DataFrame: {e}")
        raise


def convert_columns_to_date(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Convierte las columnas de tipo string a tipo datetime con formato 'YYYY-MM-DD'."""

    for column in columns:
        try:
            df[column] = pd.to_datetime(df[column], format="%d-%m-%Y", errors="coerce")

        except KeyError as e:
            print(f"La columna '{column}' no se encuentra en el DataFrame: {e}")
            raise
        except ValueError as e:
            print(f"La columna '{column}' no se encuentra en el DataFrame: {e}")
            raise
    return df


def convert_columns_to_float(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """Convierte todas las columnas excepto la de fecha a tipo float, manejando errores."""
    for column in df.columns:
        if column != date_column:
            # Intentamos convertir cada columna a float
            try:
                # Primero, intentamos convertir valores no numéricos a NaN
                df[column] = pd.to_numeric(df[column], errors="coerce")
            except KeyError as e:
                print(f"La columna '{column}' no se encuentra en el DataFrame: {e}")
                raise
            except ValueError as e:
                print(f"La columna '{column}' no se encuentra en el DataFrame: {e}")
                raise
    return df


if __name__ == "__main__":
    pass
