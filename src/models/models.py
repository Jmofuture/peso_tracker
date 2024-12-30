"""Modelo de datos"""

import os
import math
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def insert_data_from_dataframe(df: pd.DataFrame) -> None:
    """Inserta datos de un DataFrame en la tabla 'peso_tracker' en Supabase."""

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
                supabase.table("peso_tracker")
                .upsert(records, on_conflict=["date"])
                .execute()
            )
            print(f"Se insertaron {len(records)} registros en Supabase.")
        except Exception as e:
            print(f"Error al insertar los datos en Supabase: {str(e)}")
    else:
        print("No hay registros válidos para insertar.")


if __name__ == "__main__":
    print("Modelo listo para recibir datos.")
