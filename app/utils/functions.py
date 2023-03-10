import pandas as pd
import numpy as np

def calculateVolumetrics(data):
    #saving the dates in a variable as datetime 
    datetimes = pd.to_datetime(data['REF_DATE'])
    vol = datetimes.groupby(datetimes.dt.to_period("M")).agg('count')
    return vol.to_json()

def calculateProbability(data):
    #using pandas to read the pickle file (using absolute path in my pc) 
    model = pd.read_pickle("/mnt/d/coding/neurotech/ps/Neurotech-challenge-data-scientist/ml_models/model.pkl")

    #getting the dataframe ready for the prediction
    data.fillna(np.NaN, inplace=True)
    columns_to_drop = ['REF_DATE', 'TARGET']
    data_ready = data.drop(columns_to_drop, axis = 1, errors='ignore')
    
    #using the predict_probability class to infer the area under the curve for the given model and dataset
    return model.predict_proba(data_ready)[:,1]