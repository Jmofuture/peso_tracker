"""Modelo y Esquema de datos"""

from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field, Date
from pydantic import BaseModel


class ExchangeRate(SQLModel, table=True):
    """
    Modelo que representa la tabla de tasas de cambio en la base de datos.

    Atributos:
        date (date): La fecha en que se registró la tasa de cambio. No puede ser nula.
        usd_buy (Optional[float]): La tasa de compra del dólar estadounidense.
        usd_sell (Optional[float]): La tasa de venta del dólar estadounidense.
        ebrou_usd_buy (Optional[float]): La tasa de compra del dólar estadounidense en EBRou.
        ebrou_usd_sell (Optional[float]): La tasa de venta del dólar estadounidense en EBRou.
        eur_buy (Optional[float]): La tasa de compra del euro.
        eur_sell (Optional[float]): La tasa de venta del euro.
        ars_buy (Optional[float]): La tasa de compra del peso argentino.
        ars_sell (Optional[float]): La tasa de venta del peso argentino.
        brl_buy (Optional[float]): La tasa de compra del real brasileño.
        brl_sell (Optional[float]): La tasa de venta del real brasileño.
    """

    date: Date = Field(primary_key=True)
    usd_buy: Optional[float] = Field(default=None)
    usd_sell: Optional[float] = Field(default=None)
    ebrou_usd_buy: Optional[float] = Field(default=None)
    ebrou_usd_sell: Optional[float] = Field(default=None)
    eur_buy: Optional[float] = Field(default=None)
    eur_sell: Optional[float] = Field(default=None)
    ars_buy: Optional[float] = Field(default=None)
    ars_sell: Optional[float] = Field(default=None)
    brl_buy: Optional[float] = Field(default=None)
    brl_sell: Optional[float] = Field(default=None)


class ExchangeRateOut(BaseModel):
    """
    Esquema que define la estructura de salida de las tasas de cambio para la API.

    Atributos:
        date (date): La fecha en que se registró la tasa de cambio.
        usd_buy (Optional[float]): La tasa de compra del dólar estadounidense.
        usd_sell (Optional[float]): La tasa de venta del dólar estadounidense.
        ebrou_usd_buy (Optional[float]): La tasa de compra del dólar estadounidense en EBRou.
        ebrou_usd_sell (Optional[float]): La tasa de venta del dólar estadounidense en EBRou.
        eur_buy (Optional[float]): La tasa de compra del euro.
        eur_sell (Optional[float]): La tasa de venta del euro.
        ars_buy (Optional[float]): La tasa de compra del peso argentino.
        ars_sell (Optional[float]): La tasa de venta del peso argentino.
        brl_buy (Optional[float]): La tasa de compra del real brasileño.
        brl_sell (Optional[float]): La tasa de venta del real brasileño.
    """

    date: date
    usd_buy: Optional[float] = None
    usd_sell: Optional[float] = None
    ebrou_usd_buy: Optional[float] = None
    ebrou_usd_sell: Optional[float] = None
    eur_buy: Optional[float] = None
    eur_sell: Optional[float] = None
    ars_buy: Optional[float] = None
    ars_sell: Optional[float] = None
    brl_buy: Optional[float] = None
    brl_sell: Optional[float] = None

    class Config:
        """
        Configuración adicional para el esquema de salida.
        - orm_mode = True permite que Pydantic convierta los modelos ORM (SQLModel) en diccionarios.
        """

        orm_mode = True
