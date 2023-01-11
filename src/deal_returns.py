import pandas as pd
from . import contants

data = pd.read_csv(contants.returesFile,index_col=(0),parse_dates=True)
data.insert(len(data.columns),column='week',value=list(data.index.week))
sumData = data.groupby('week').agg('mean')
columnName = sumData.columns.to_list() 

def getReturnsByCode(code):
    if code in columnName:
        _arr = []
        weekList = list(sumData.index)
        codeReturn = sumData[code]
        for i in range(1,weekList[-1]):
            if(i in weekList):
                _arr.append(codeReturn[i])
            else:
             _arr.append(0)
        return _arr
    else :
        return False