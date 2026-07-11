#aula 12 estraindo dados do FRED

#### DEVE INSTALAR PRIMEIRO:
## pip install pandas_datareader

import matplotlib.pyplot as fig
import datetime as dt
import pandas_datareader.data as web

inicio=dt.datetime(1970,1,1)
fim=dt.datetime(2025,8,1)

df1=web.DataReader('DGS10','fred',inicio,fim)   # TITULO DE 10 ANOS AMERICANO

# YAHOO não se encontra disponível no momento (ver método da Aula 11)
#df1=web.DataReader('^DJI','yahoo',inicio,fim)   

# média móvel de 500 dias
df1['med_mov']=df1['DGS10'].rolling(window=500,min_periods=0).mean()

ax=fig.subplot(111)
ax.plot(df1.index,df1['DGS10'],color='black',alpha=0.5)
ax.plot(df1.index,df1['med_mov'],color='black')
ax.set_title('Tesouro EUA - venc 10 anos (10-year Treasury)',fontsize=18,weight='bold')
