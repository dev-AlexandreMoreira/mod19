# código de geração do gráfico
import pandas as pd
import seaborn as sns
tabela = pd.read_csv("gasolina.csv")

tabela.head()

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=tabela, x="dia", y="venda", palette="bright")
  grafico.set(title='Média do preço da Gasolina em SP - JUL/21', xlabel='Dia', ylabel='Média do preço em (R$)');
