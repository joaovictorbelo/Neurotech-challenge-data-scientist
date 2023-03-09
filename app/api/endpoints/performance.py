"""Endpoint para cálculo de Performance."""
from fastapi import APIRouter
from sklearn.metrics import  roc_auc_score
from ..models.record_model import Record
import pandas as pd
from fastapi.encoders import jsonable_encoder
import json
import numpy as np

router = APIRouter(prefix="/performance")

def countRecordsByMonth(data):
    return data.groupby(data.dt.to_period("M")).agg('count')

def calculatePerformance(data, model):
    #getting the dataframe ready for the prediction
    data.fillna(np.NaN, inplace=True)
    target_scores = data['TARGET'].to_list()
    columns_to_drop = ['REF_DATE', 'TARGET']
    data_test = data.drop(columns_to_drop, axis = 1)
    
    #using the predict_probability class to infer the area under the curve for the given model and dataset
    test_prob=model.predict_proba(data)[:,1]
    return roc_auc_score(target_scores,test_prob)

@router.post("/")
async def Performance(data: list[Record]):
    #reading the data and saving it in a dataframe
    convertedData = jsonable_encoder(data)
    df = pd.json_normalize(convertedData)
    
    #saving the dates in a variable as datetime 
    datetimes = pd.to_datetime(df['REF_DATE'])
    #getting the volumetrics
    volumetrics = countRecordsByMonth(datetimes).to_json()
    
    model = pd.read_pickle("/mnt/d/coding/neurotech/ps/Neurotech-challenge-data-scientist/ml_models/model.pkl")

    perf = calculatePerformance(df, model)

    print('ROC auc for test dataframe:', perf)
    
    #returning
    response = {
        "volumetria": json.loads(volumetrics),
        "performance": perf
    }
    return response