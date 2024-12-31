"""Endpoints"""

from datetime import date
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schema import ExchangeRateOut
from api.schema import ExchangeRate
from api.db_dependencies import get_session


app = FastAPI()

# Crear el router para las rutas
router = APIRouter()


@router.get("/exchange-rates/{exchange_date}", response_model=ExchangeRateOut)
def get_exchange_rate(exchange_date: date, session: Session = Depends(get_session)):
    """
    Obtiene la tasa de cambio para una fecha específica.

    Este endpoint consulta la base de datos para obtener la tasa de cambio
    de una fecha dada. Si la tasa de cambio no se encuentra en la base de
    datos, se devuelve un error 404.

    Args:
        exchange_date (date): La fecha para la cual se solicita la tasa de cambio.
        session (Session): La sesión de base de datos utilizada para la consulta.

    Returns:
        ExchangeRateOut: Un objeto que contiene la tasa de cambio para la fecha solicitada.

    Raises:
        HTTPException: Si no se encuentra la tasa de cambio para la fecha proporcionada,
    se lanza un error 404 con el mensaje "Exchange rate not found for the given date".
    """
    db_rate = (
        session.query(ExchangeRate).filter(ExchangeRate.date == exchange_date).first()
    )
    if db_rate is None:
        raise HTTPException(
            status_code=404, detail="Exchange rate not found for the given date"
        )
    return db_rate
