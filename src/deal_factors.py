import pandas as pd
from . import contants

setting ={'first':True}
data = pd.read_csv(contants.factorFile,index_col=(0),parse_dates=True)
def getFactorsSum():
    if(setting['first']):
        data.insert(len(data.columns),column='week',value=list(data.index.isocalendar().week))
        setting['first'] = False
    sumData = data.groupby('week').agg('mean')
    return sumData
