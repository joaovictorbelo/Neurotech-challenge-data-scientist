import pandas as pd
from sklearn.metrics import  roc_auc_score
import numpy as np

def calculateVolumetrics(data):
    #saving the dates in a variable as datetime 
    datetimes = pd.to_datetime(data['REF_DATE'])
    vol = datetimes.groupby(datetimes.dt.to_period("M")).agg('count')
    return vol.to_json()

def calculatePerformance(data, model):
    #getting the dataframe ready for the prediction
    data.fillna(np.NaN, inplace=True)
    target_scores = data['TARGET'].to_list()
    columns_to_drop = ['REF_DATE', 'TARGET']
    data_test = data.drop(columns_to_drop, axis = 1)
    
    #using the predict_probability class to infer the area under the curve for the given model and dataset
    test_prob=model.predict_proba(data)[:,1]
    return roc_auc_score(target_scores,test_prob)
