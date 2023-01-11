from os import path

strs = '[a-zA-Z0-9’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+'

postxt = path.join(path.dirname(path.dirname(path.realpath(__file__))),'assets','正面词汇.txt')
negext = path.join(path.dirname(path.dirname(path.realpath(__file__))),'assets','负面词汇.txt')

excel = path.join(path.dirname(path.dirname(path.realpath(__file__))),'assets','data.xlsx')
factorFile = path.join(path.dirname(path.dirname(path.realpath(__file__))),'assets','threefactors.csv')
returesFile = path.join(path.dirname(path.dirname(path.realpath(__file__))),'assets','returns.csv')
shiborFile = path.join(path.dirname(path.dirname(path.realpath(__file__))),'assets','shibor.csv')