import os
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, Column, Float, Date, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError, OperationalError
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "default.db")
engine = create_engine("sqlite:///database.db", echo=True)


# Definir base de datos
Base = declarative_base()


class DailyExchangeRate(Base):
    __tablename__ = "daily_exchange_rates"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
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
    """Inserta datos de un DataFrame en la tabla 'daily_exchange_rates'."""
    session = Session()
    try:
        # Reemplazar '..' con None
        df = df.replace("..", 0.0)

        # Asegurarse de que las fechas estén en el formato correcto
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%d-%m-%Y")

        records = []

        for _, row in df.iterrows():
            try:
                # Convertir fecha a formato correcto
                date = datetime.strptime(str(row["date"]), "%d-%m-%Y").date()

                # Crear objeto para insertar, manejando valores nulos
                record = DailyExchangeRate(
                    date=date,
                    usd_buy=float(row["usd_buy"])
                    if row.get("usd_buy") not in [None, ""]
                    else None,
                    usd_sell=float(row["usd_sell"])
                    if row.get("usd_sell") not in [None, ""]
                    else None,
                    ebrou_usd_buy=float(row["ebrou_usd_buy"])
                    if row.get("ebrou_usd_buy") not in [None, ""]
                    else None,
                    ebrou_usd_sell=float(row["ebrou_usd_sell"])
                    if row.get("ebrou_usd_sell") not in [None, ""]
                    else None,
                    eur_buy=float(row["eur_buy"])
                    if row.get("eur_buy") not in [None, ""]
                    else None,
                    eur_sell=float(row["eur_sell"])
                    if row.get("eur_sell") not in [None, ""]
                    else None,
                    ars_buy=float(row["ars_buy"])
                    if row.get("ars_buy") not in [None, ""]
                    else None,
                    ars_sell=float(row["ars_sell"])
                    if row.get("ars_sell") not in [None, ""]
                    else None,
                    brl_buy=float(row["brl_buy"])
                    if row.get("brl_buy") not in [None, ""]
                    else None,
                    brl_sell=float(row["brl_sell"])
                    if row.get("brl_sell") not in [None, ""]
                    else None,
                )
                records.append(record)

            except ValueError as ve:
                print(f"Error al procesar la fila: {row.to_dict()} - {ve}")

        # Insertar todos los registros de una vez
        if records:
            session.bulk_save_objects(records)
            session.commit()
            print(f"Se insertaron {len(records)} registros en la base de datos.")
        else:
            print("No hay registros válidos para insertar.")

    except IntegrityError as ie:
        session.rollback()
        print(f"Error de integridad en la base de datos: {str(ie)}")

    except OperationalError as oe:
        session.rollback()
        print(f"Error operativo en la base de datos: {str(oe)}")

    except Exception as e:
        session.rollback()
        print(f"Error inesperado al insertar los datos: {str(e)}")

    finally:
        session.close()


if __name__ == "__main__":
    print("Modelo listo para recibir datos.")
