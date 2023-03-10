"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter
import pandas as pd
import json
from sklearn.metrics import  roc_auc_score
from ..models.record_model import Record
from fastapi.encoders import jsonable_encoder
from ...utils.functions import (calculateVolumetrics, calculateProbability)

router = APIRouter(prefix="/performance")

@router.post("/")
async def Performance(data: list[Record]):
    #reading the data and saving it in a dataframe
    convertedData = jsonable_encoder(data)
    df = pd.json_normalize(convertedData)
    target_scores = df['TARGET'].to_list()

    #getting the volumetrics
    volumetrics = calculateVolumetrics(df)

    test_prob = calculateProbability(df)
    #print('ROC auc for test dataframe:', perf)
    
    perf = roc_auc_score(target_scores,test_prob)
    
    #returning
    response = {
        "volumetria": json.loads(volumetrics),
        "performance": perf
    }
    return response