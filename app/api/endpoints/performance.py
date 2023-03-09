"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter
from ..models.record_model import Record
import pandas as pd
from fastapi.encoders import jsonable_encoder
from fastapi import Response

router = APIRouter(prefix="/performance")

def countRecordsByMonth(data):
    return data.groupby(data.dt.to_period("M")).agg('count')

@router.post("/")
async def Performance(data: list[Record]):
    convertedData = jsonable_encoder(data)
    df = pd.json_normalize(convertedData)
    datetimes = pd.to_datetime(df['REF_DATE'])
    volumetrics = countRecordsByMonth(datetimes).to_json()
    return Response(content=volumetrics, media_type="application/json")