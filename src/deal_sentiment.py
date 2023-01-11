# -*- coding: utf-8 -*-
import pandas as pd
import jieba
import re
from . import contants

data = pd.read_excel(contants.excel,index_col=(0),parse_dates=True)

# 插入周数
data.insert(len(data.columns),column='week',value=list(data.index.week))

def getCodeNumArr():
    _codeArr = []
    for i in data['code']:
        if  i not in _codeArr:
            _codeArr.append(i)
    return _codeArr
    

def insertPostiveAndNegative():

    titleList = data['title'].tolist()
    positive_words = pd.read_table(contants.postxt,encoding='gbk')
    positive_words = list(positive_words['词汇'])
    negative_words = pd.read_table(contants.negext,encoding='gbk')
    negative_words = list(negative_words['词汇'])

    positiveNum = []
    negativeNum = []
    
    for text in titleList:
        positive = 0
        negative = 0
        wordList = jieba.cut(re.sub(contants.strs, "", text))

        for i in wordList:
            if i in positive_words:
                positive+=1
            if i in negative_words:
                negative += 1

        positiveNum.append(positive)
        negativeNum.append(negative)

    data.insert(len(data.columns),column='positive',value=positiveNum)
    data.insert(len(data.columns),column='negative',value=negativeNum)

# 情绪分
def getSentiment(pos,neg):
    return (pos-neg)/(1+pos+neg)



def getSumData(code):
    codeData = data[data['code']==code]
    sumData = codeData.groupby('week').agg('sum')
    return sumData


def CodeWeekSentimentList(sumData):
    _arr = []
    dataList = list(sumData.index)
    for i in range(1,dataList[-1]):
        if(i in dataList):
            pos = sumData['positive'][i]
            neg = sumData['negative'][i]
            _arr.append(getSentiment(pos,neg))
        else:
            _arr.append(0)
    return _arr