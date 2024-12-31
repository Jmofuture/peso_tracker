"""Modelo y Esquema de datos"""

from datetime import date
from typing import Optional
from pydantic import BaseModel, model_validator


class ExchangeRate(BaseModel):
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


class ExchangeRateUSD(BaseModel):
    """
    Modelo para representar las tasas de cambio del USD.
    """

    date: str
    usd_buy: Optional[float]
    usd_sell: Optional[float]
    spread: Optional[float] = None

    @model_validator(mode="before")
    @classmethod
    def calculate_spread(cls, values):
        """
        Calcula el Spread del día
        """
        usd_buy = values.get("usd_buy")
        usd_sell = values.get("usd_sell")

        if usd_buy is not None and usd_sell is not None:
            values["spread"] = usd_sell - usd_buy
        return values

    class Config:
        """
        Configuración adicional para el esquema de salida.
        - orm_mode = True permite que Pydantic convierta los modelos ORM (SQLModel) en diccionarios.
        """

        orm_mode = True


class ExchangeRateEUR(BaseModel):
    """
    Modelo para representar las tasas de cambio del EUR.
    """

    date: str
    eur_buy: Optional[float]
    eur_sell: Optional[float]
    spread: Optional[float] = None

    @model_validator(mode="before")
    @classmethod
    def calculate_spread(cls, values):
        """
        Calcula el Spread del día
        """
        eur_buy = values.get("eur_buy")
        eur_sell = values.get("eur_sell")

        if eur_buy is not None and eur_sell is not None:
            values["spread"] = eur_sell - eur_buy
        return values

    class Config:
        """
        Configuración adicional para el esquema de salida.
        - orm_mode = True permite que Pydantic convierta los modelos ORM (SQLModel) en diccionarios.
        """

        orm_mode = True


class ExchangeRateBRL(BaseModel):
    """
    Modelo para representar las tasas de cambio del BRL.
    """

    date: str
    brl_buy: Optional[float]
    brl_sell: Optional[float]
    spread: Optional[float] = None

    @model_validator(mode="before")
    @classmethod
    def calculate_spread(cls, values):
        """
        Calcula el Spread del día
        """
        brl_buy = values.get("brl_buy")
        brl_sell = values.get("brl_sell")

        if brl_buy is not None and brl_sell is not None:
            values["spread"] = brl_sell - brl_buy
        return values

    class Config:
        """
        Configuración adicional para el esquema de salida.
        - orm_mode = True permite que Pydantic convierta los modelos ORM (SQLModel) en diccionarios.
        """

        orm_mode = True


class ExchangeRateARS(BaseModel):
    """
    Modelo para representar las tasas de cambio del ARS.
    """

    date: str
    ars_buy: Optional[float]
    ars_sell: Optional[float]
    spread: Optional[float] = None

    @model_validator(mode="before")
    @classmethod
    def calculate_spread(cls, values):
        """
        Calcula el Spread del día
        """
        ars_buy = values.get("ars_buy")
        ars_sell = values.get("ars_sell")

        if ars_buy is not None and ars_sell is not None:
            values["spread"] = ars_sell - ars_buy
        return values

    class Config:
        """
        Configuración adicional para el esquema de salida.
        - orm_mode = True permite que Pydantic convierta los modelos ORM (SQLModel) en diccionarios.
        """

        orm_mode = True


class ExchangeRateBROU(BaseModel):
    """
    Modelo para representar las tasas de cambio del dólar en el Banco BROU (EBROU).
    """

    date: str
    ebrou_usd_buy: Optional[float]
    ebrou_usd_sell: Optional[float]
    spread: Optional[float] = None

    @model_validator(mode="before")
    @classmethod
    def calculate_spread(cls, values):
        """
        Calcula el Spread del día
        """
        ebrou_usd_buy = values.get("ebrou_usd_buy")
        ebrou_usd_sell = values.get("ebrou_usd_sell")

        if ebrou_usd_buy is not None and ebrou_usd_sell is not None:
            values["spread"] = ebrou_usd_sell - ebrou_usd_buy
        return values

    class Config:
        """
        Configuración adicional para el esquema de salida.
        - orm_mode = True permite que Pydantic convierta los modelos ORM (SQLModel) en diccionarios.
        """

        orm_mode = True
