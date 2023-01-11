import pandas as pd
from . import contants
data = pd.read_csv(contants.shiborFile,index_col=(0),parse_dates=True)
data.insert(len(data.columns),column='week',value=list(data.index.week))
sumData = data.groupby('week').agg('mean').iloc[0:51]

def getShiborArr():
    return sumData['shibor'].to_list()
