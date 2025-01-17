"""Modelo de datos"""

import math
from datetime import datetime
import pandas as pd


def insert_data_from_dataframe(df: pd.DataFrame, dbclient, table_name: str) -> None:
    """
    Insert data from a pandas DataFrame into a Supabase table.

    Args:
        df (pd.DataFrame): DataFrame with the data to be inserted.
        dbclient: Supabase client instance.
        table_name (str): Name of the table in Supabase.

    Returns:
        None
    """
    if df is None:
        print("El DataFrame está vacío o no se cargó correctamente.")
        return

    df.replace("..", None)

    df = df.map(lambda x: None if isinstance(x, float) and math.isnan(x) else x)

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    records = []

    for _, row in df.iterrows():
        try:
            date = datetime.strptime(str(row["date"]), "%Y-%m-%d").date()

            record = {
                "date": date.strftime("%Y-%m-%d"),
                "usd_buy": None if pd.isna(row["usd_buy"]) else float(row["usd_buy"]),
                "usd_sell": None
                if pd.isna(row["usd_sell"])
                else float(row["usd_sell"]),
                "ebrou_usd_buy": None
                if pd.isna(row["ebrou_usd_buy"])
                else float(row["ebrou_usd_buy"]),
                "ebrou_usd_sell": None
                if pd.isna(row["ebrou_usd_sell"])
                else float(row["ebrou_usd_sell"]),
                "eur_buy": None if pd.isna(row["eur_buy"]) else float(row["eur_buy"]),
                "eur_sell": None
                if pd.isna(row["eur_sell"])
                else float(row["eur_sell"]),
                "ars_buy": None if pd.isna(row["ars_buy"]) else float(row["ars_buy"]),
                "ars_sell": None
                if pd.isna(row["ars_sell"])
                else float(row["ars_sell"]),
                "brl_buy": None if pd.isna(row["brl_buy"]) else float(row["brl_buy"]),
                "brl_sell": None
                if pd.isna(row["brl_sell"])
                else float(row["brl_sell"]),
            }

            records.append(record)

        except ValueError as ve:
            print(f"Error al procesar la fila: {row.to_dict()} - {ve}")

    if records:
        try:
            response = (
                dbclient.table(table_name)
                .upsert(records, on_conflict=["date"])
                .execute()
            )

            # Imprimir todo el objeto de respuesta para depuración
            print("Respuesta completa de Supabase:")
            print(response)

            # Manejar errores o verificar éxito
            if hasattr(response, "data") and response.data:
                print(f"Inserted {len(records)} records into Supabase")
            elif hasattr(response, "error") and response.error:
                print(f"Error en la respuesta de Supabase: {response.error}")
            else:
                print("Respuesta inesperada de Supabase.")
        except Exception as e:
            print(f"Error inserting data into Supabase: {str(e)}")
    else:
        print("No valid records to insert")


if __name__ == "__main__":
    print("Model ready to receive data")
