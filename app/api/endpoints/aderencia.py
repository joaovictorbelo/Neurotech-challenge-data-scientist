"""Endpoint para cálculo de aderência."""
import json
from fastapi import APIRouter
import numpy as np
import pandas as pd
from scipy import stats
from ..models.path_model import Path
from ..utils.perf_functions import calculateProbability

router = APIRouter(prefix="/aderencia")

@router.post("/")
async def Performance(data: Path):
    #reading the test dataset as a dataframe, it will be used as comparison
    test_df = pd.read_csv('/mnt/d/coding/neurotech/ps/Neurotech-challenge-data-scientist/datasets/test.gz', compression='gzip')
    
    #reading the passed path as a dataframe (using the absolute path)
    chosen_df = pd.read_csv('/mnt/d/coding/neurotech/ps' + data.path, compression='gzip')
    
    #treat the error in the 'out of time' dataset
    if (data.path.endswith('oot.gz') or data.path.endswith('oot.csv')):
        chosen_df['VAR121'] = chosen_df['VAR121'].replace('MUITO PROXIMO',np.NAN)
    
    #calculating the propabilities for both the test and the inputed datasets
    test_prob = calculateProbability(test_df)
    chosen_prob = calculateProbability(chosen_df)
     
    #getting the distance of probability by using the ks method available in scipy
    result = stats.ks_2samp(test_prob, chosen_prob)
    
    answer = {
        "aderencia": result[0]
    }
    
    return answer