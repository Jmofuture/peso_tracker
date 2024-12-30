"""Modelo de datos"""

import os
import math
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, Column, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# DATABASE_URL = os.getenv("DATABASE_URL", "default.db")
engine = create_engine("sqlite:///database.db", echo=False)

Base = declarative_base()


class DailyExchangeRate(Base):
    __tablename__ = "daily_exchange_rates"
    date = Column(
        Date,
        primary_key=True,
    )
    usd_buy = Column(Float)
    usd_sell = Column(Float)
    ebrou_usd_buy = Column(Float)
    ebrou_usd_sell = Column(Float)
    eur_buy = Column(Float)
    eur_sell = Column(Float)
    ars_buy = Column(Float)
    ars_sell = Column(Float)
    brl_buy = Column(Float)
    brl_sell = Column(Float)

    def serialize(self):
        """Método para serializar los datos."""
        return {
            "date": self.date,
            "usd_buy": self.usd_buy,
            "usd_sell": self.usd_sell,
            "ebrou_usd_buy": self.ebrou_usd_buy,
            "ebrou_usd_sell": self.ebrou_usd_sell,
            "eur_buy": self.eur_buy,
            "eur_sell": self.eur_sell,
            "ars_buy": self.ars_buy,
            "ars_sell": self.ars_sell,
            "brl_buy": self.brl_buy,
            "brl_sell": self.brl_sell,
        }


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)


def insert_data_from_dataframe(df: pd.DataFrame) -> None:
    """Inserta datos de un DataFrame en la tabla 'peso_tracker' en Supabase."""

    if df is None:
        print("El DataFrame está vacío o no se cargó correctamente.")
        return

    df.replace("..", None, inplace=True)

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
