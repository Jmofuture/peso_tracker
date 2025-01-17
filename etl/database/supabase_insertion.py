"""Modelo de datos"""

import math
from datetime import datetime
import pandas as pd


def insert_data_from_dataframe(df: pd.DataFrame, dbclient, table_name: str) -> None:
    """
    Insert data from a pandas DataFrame into a Supabase table.

    This function processes a DataFrame containing currency exchange data,
    cleans and formats the data, and inserts it into the "peso_tracker" table
    in a Supabase database. Rows with conflicting "date" values are upserted.

    Args:
        df (pd.DataFrame):
            The DataFrame containing the data to be inserted. It should have the
            following columns:
            - "date": The date of the record (string or datetime).
            - "usd_buy", "usd_sell", "ebrou_usd_buy", "ebrou_usd_sell",
              "eur_buy", "eur_sell", "ars_buy", "ars_sell", "brl_buy", "brl_sell":
              Numeric columns representing exchange rates for different currencies.
        dbclient:
            A Supabase client instance used to interact with the database.

    Returns:
        None

    Raises:
        ValueError:
            If a row in the DataFrame contains invalid data that cannot be processed.
        Exception:
            If there is an error while inserting data into the database.

    Notes:
        - The function replaces any occurrence of ".." in the DataFrame with `None`.
        - NaN values are also replaced with `None` for compatibility with the database.
        - Dates are converted to the format "YYYY-MM-DD".
        - Invalid rows (e.g., rows with parsing errors) are skipped, and a warning is printed.
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

            if hasattr(response, "data"):
                print(f"Inserted {len(response.data)} records into Supabase.")
            elif hasattr(response, "error"):
                print(f"Error en la respuesta de Supabase: {response.error}")
            else:
                print(f"Respuesta inesperada de Supabase: {response}")

        except Exception as e:
            print(f"Error inserting data into Supabase: {str(e)}")
    else:
        print("No valid records to insert")


if __name__ == "__main__":
    print("Model ready to receive data")
