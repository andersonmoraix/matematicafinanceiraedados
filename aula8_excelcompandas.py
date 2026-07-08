#aula 8 aplicacao com excel e pandas

import pandas as pd
dados=pd.read_excel('XYZW3.xlsx',sheet_name='Planilha2')
df=pd.DataFrame(dados)

print(df)

print(df.head(n=10))
print(df.FECHAMENTO.head(n=10))

df[df['FECHAMENTO']>29.5]


df2=df[(df['FECHAMENTO']<29.0) & (df['ABERTURA']>29.0)]

# pode usar sort_values

df2.sort_values(by='ABERTURA',ascending=False)  # outro exemplo de mineracao de dados
