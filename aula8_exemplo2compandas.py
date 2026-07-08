#aula8, estrutura mais elaborada com pandas

# Pandas - DataFrame
# É como a tabela dinâmica do Excel
# Com Series, não podemos colocar duas colecoes de dados
# Com DataFrame, podemos colocar mais colecoes


import pandas as pd

info=pd.DataFrame({'Produto':['Tijolo','Tinta','Solvente','Telhas','Cimento'],
'Preço':[3.3,4.5,12,27,45.6],'Qtde':[10,12,23,34,4],'Custo':[0.5,1.2,1.4,12,12]})

print(info)

#######################
# Atenção: digite os comandos abaixo no prompt
# para poder visualizar melhor a análise

info['Produto']
info['Preço']

info.Produto   # é o mesmo que info['Produto'] 
info.Preço

info.columns   # nomes das colunas

info.sort_values(by='Produto')  # ordem crescente
info.sort_values(by='Preço')
info.sort_values(by='Produto',ascending=False)  # descrescente

info['Custo']>1.2       # Lista true/false dos itens tais que custo>1.2
info[info['Custo']>1.2]  # Lista dos *itens* tais que custo>1.2

info[(info['Custo']>1.2) & (info['Qtde']>10)]