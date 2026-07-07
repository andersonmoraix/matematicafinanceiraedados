#aula 6 importando arquivos da planilha

import xlrd   # uma das bibliotecas disponiveis para Excel
import statistics as st
import matplotlib.pyplot as gr

wb=xlrd.open_workbook('dados.xls')   # planilha Excel com 2 colunas de dados

p=wb.sheet_by_name('Planilha1')

x=p.col_values(0) 
y=p.col_values(1)

linha=p.nrows   # número de linhas
coluna=p.ncols   # número de colunas

# Ilustrando a criação de uma lista 'dados', 
# onde cada elemento da lista é uma lista

dados=[]

for i in range(coluna):
    coldados=p.col_values(i)
    dados.append(coldados)

media=st.mean(dados[1][:])  # coluna b, todos os dados
desvio=st.pstdev(dados[1][:])

gr.subplot(211)

gr.hist(dados[1][:],bins=7)
gr.xlabel('classes')
gr.ylabel('freq')

### boxplot - ajudar a resumir estatísticas
# mostra valor do dado minimo, maximo, mediano, tamanho do desv padrao
# É a curva normal "vista de cima"
# no Excel - também pode ser feito (não tão simples)

gr.subplot(212)
gr.boxplot(dados[1][:])
