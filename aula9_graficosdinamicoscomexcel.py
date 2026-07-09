#aula 9 graficos dinamicos

#Gráficos dinâmicos com DataFrames (pandas)

import matplotlib.pyplot as gr
import pandas as pd
import time

df=pd.read_excel('XYZW3.xlsx','Planilha2')

n=len(df.DATA)

ax=gr.subplot(111)

for i in range(n):
 ax.plot(df[0:i].DATA,df[0:i].ABERTURA,'-k')
 gr.gcf().autofmt_xdate()    # inclina 45 graus

 gr.pause(0.1)