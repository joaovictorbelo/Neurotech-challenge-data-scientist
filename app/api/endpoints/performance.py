"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter
from ..models.record_model import Record

router = APIRouter(prefix="/performance")

@router.post("/")
async def teste(data: Record):
    convertedData = Record.parse_obj(data)
    return convertedData.REF_DATE