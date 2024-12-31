"""Endpoints"""

import os
from typing import List
import uvicorn
from dotenv import load_dotenv
from supabase import create_client, Client
from fastapi import FastAPI, APIRouter, HTTPException
from api.models.schema import (
    ExchangeRateUSD,
    ExchangeRateBROU,
    ExchangeRateEUR,
    ExchangeRateBRL,
    ExchangeRateARS,
)


load_dotenv()

app = FastAPI()
router = APIRouter()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


app = FastAPI(
    title="Exchange Rates API",
    description="API para obtener tipos de cambio del Peso Uruguayo / USD / EUR / BRL / ARS",
    version="1.0.0",
)


app.include_router(router, prefix="/api/v1")


@app.get("/exchange-rates/brou", response_model=List[ExchangeRateBROU])
async def get_exchange_brou():
    """
    Extrae la cotizacion del USD con respecto al Peso UY
    """
    response = (
        supabase.table("usd_brou_rate")
        .select("date, ebrou_usd_buy, ebrou_usd_sell")
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="No se encontraron datos")

    try:
        rates = [ExchangeRateBROU(**item) for item in response.data]
        return rates
    except HTTPException as e:
        print(status_code=500, detail=f"Error al procesar los datos: {e}")


@app.get("/exchange-rates/brou/week", response_model=List[ExchangeRateBROU])
async def get_exchange_last_week():
    """
    Extrae la cotizacion del USD con respecto al Peso UY
    """
    response = (
        supabase.table("usd_brou_rate")
        .select("date, ebrou_usd_buy, ebrou_usd_sell")
        .order("date", desc=True)
        .limit(7)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="No se encontraron datos")

    try:
        rates = [ExchangeRateBROU(**item) for item in response.data]
        return rates
    except HTTPException as e:
        print(status_code=500, detail=f"Error al procesar los datos: {e}")


###
@app.get("/exchange-rates/usd", response_model=List[ExchangeRateUSD])
async def get_exchange_usd():
    """
    Extrae la cotizacion del USD con respecto al Peso UY
    """
    response = supabase.table("usd_rate").select("date, usd_buy, usd_sell").execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="No se encontraron datos")

    try:
        rates = [ExchangeRateUSD(**item) for item in response.data]
        return rates
    except HTTPException as e:
        print(status_code=500, detail=f"Error al procesar los datos: {e}")


@app.get("/exchange-rates/eur", response_model=List[ExchangeRateEUR])
async def get_exchange_eur():
    """
    Extrae la cotizacion del EUR con respecto al Peso UY
    """
    response = supabase.table("eur_rate").select("date, eur_buy, eur_sell").execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="No se encontraron datos")

    try:
        rates = [ExchangeRateEUR(**item) for item in response.data]
        return rates
    except HTTPException as e:
        print(status_code=500, detail=f"Error al procesar los datos: {e}")


@app.get("/exchange-rates/brl", response_model=List[ExchangeRateBRL])
async def get_exchange_brl():
    """
    Extrae la cotizacion del BRL con respecto al Peso UY
    """
    response = supabase.table("brl_rate").select("date, brl_buy, brl_sell").execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="No se encontraron datos")

    try:
        rates = [ExchangeRateBRL(**item) for item in response.data]
        return rates
    except HTTPException as e:
        print(status_code=500, detail=f"Error al procesar los datos: {e}")


@app.get("/exchange-rates/ars", response_model=List[ExchangeRateARS])
async def get_exchange_ars():
    """
    Extrae la cotizacion del ARS con respecto al Peso UY
    """
    response = supabase.table("ars_rate").select("date, ars_buy, ars_sell").execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="No se encontraron datos")

    try:
        rates = [ExchangeRateARS(**item) for item in response.data]
        return rates
    except HTTPException as e:
        print(status_code=500, detail=f"Error al procesar los datos: {e}")


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
