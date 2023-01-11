# -*- coding: utf-8 -*-
import statsmodels.api as sm
from .utils import utils
from . import deal_sentiment
from . import deal_returns
from . import deal_factors
from . import deal_shibor
from . import paint
codeArr = deal_sentiment.getCodeNumArr()
# 第一题
deal_sentiment.insertPostiveAndNegative()

foo = {'min':0}

def getX(code):
    sumData = deal_sentiment.getSumData(code)
    # 第二题
    senArr = deal_sentiment.CodeWeekSentimentList(sumData)
    data = deal_factors.getFactorsSum()
    foo['min'] = utils.getLength(senArr) if utils.getLength(senArr)< utils.getLength(data.index) else -1
    data = data.iloc[0:foo['min']]
    data.insert(len(data.columns),column='sentimemt',value=senArr[0:foo['min']])
    return data


def getY(code):
    res = deal_returns.getReturnsByCode(utils.toString(code))[0:foo['min']]
    return res

def getTotal():
    #第三题
    _arr = []
    shiborArr = deal_shibor.getShiborArr()
    for stock in codeArr:
        try:
            x = getX(stock)
            y = getY(stock)
            modify_y = []
            for i in range(0,len(y)):
                modify_y.append(y[i]-shiborArr[i])

            mod = sm.OLS(modify_y,sm.add_constant(x)).fit()
            _arr.append({'code':stock,'r':mod.rsquared,'p':mod.pvalues[-1],'b4':mod.params[-1]})
        except Exception as error:
            continue
    return _arr


def runApp():
    res = getResDict()
    print(res)
    paint.paintRes(res['code'])
    print('图片已保存')


def getResDict():
    maxR = 0
    res = {}
    arr = getTotal()

    print(arr)
    for dist in arr:
        if(dist['p']<0.05 and dist['b4']>0):
            if(dist['r']>maxR):
              res = dist
              maxR = dist['r']
    
    return res