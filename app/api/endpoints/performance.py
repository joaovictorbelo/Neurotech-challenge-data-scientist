"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter
import pandas as pd
import json
from ..models.record_model import Record
from fastapi.encoders import jsonable_encoder
from ..utils.perf_functions import (calculateVolumetrics, calculatePerformance)

router = APIRouter(prefix="/performance")

@router.post("/")
async def Performance(data: list[Record]):
    #reading the data and saving it in a dataframe
    convertedData = jsonable_encoder(data)
    df = pd.json_normalize(convertedData)

    #getting the volumetrics
    volumetrics = calculateVolumetrics(df)
    
    #using pandas to read the pickle file (using absolute path in my pc) 
    model = pd.read_pickle("/mnt/d/coding/neurotech/ps/Neurotech-challenge-data-scientist/ml_models/model.pkl")

    perf = calculatePerformance(df, model)
    #print('ROC auc for test dataframe:', perf)
    
    #returning
    response = {
        "volumetria": json.loads(volumetrics),
        "performance": perf
    }
    return response