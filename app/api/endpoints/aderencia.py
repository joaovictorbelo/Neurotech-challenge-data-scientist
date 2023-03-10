"""Endpoint para cálculo de aderência."""
from fastapi import APIRouter
from ..models.path_model import Path

router = APIRouter(prefix="/aderencia")

@router.post("/")
async def Performance(path: Path):
    return path