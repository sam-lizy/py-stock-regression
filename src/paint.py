import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from . import deal_returns
from .utils import utils
def paintRes(code,window=13):
    res = deal_returns.getReturnsByCode(utils.toString(code))
    data = DataFrame(res)
    #设置索引为周数，原值改为true values
    data.rename(columns={0:'true values'},inplace=True)
    data.index.name ='week'
    #计算预测收益率,时间窗口为13
    data['predict values'] = data['true values'].rolling(window).mean()  
    #作图 
    fig = plt.figure(figsize=(12,8))
    plt.plot(data['true values'],'r--o',alpha=0.45,lw=1,markerfacecolor='none',markersize=10,label='true values') 
    plt.plot(data['predict values'],'b--x',alpha=0.45,lw=1,markerfacecolor='none',markersize=10,label='predict values') 
    plt.legend(loc = 'lower left', fontsize=15)
    plt.xticks(fontsize =20,rotation=45)
    plt.yticks (fontsize =29)
    plt.xticks (fontsize =25)
    plt.title('returns of stock'+ ' ' + utils.toString(code),size=30,loc = 'center')
    plt.savefig('I22301171_王续然', bbox_inches='tight',dpi=1080)    