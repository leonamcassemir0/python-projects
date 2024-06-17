import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('data/sales_data.csv')

"""
# .head() pega os 5 primeiros dados
print(sales.head())
# .shape pega o número de linhas e colunas do database
print(sales.shape)
# .info() traz informações técnicas de sua tabela
print(sales.info())
# .describe() traz informações relevantes dos dados de sua tabela
print(sales.describe())
# Podemos analisar uma coluna específica: variable[column].describe()
print(sales['Unit_Cost'].describe())
# Podemos pegar informações específicas do describe
print(sales.min())
"""

# Criar uma tabela simples
sales['Unit_Cost'].plot(kind='hist')
plt.xlabel("exemplo x")
plt.ylabel("exemplo y")
print(sales['Unit_Cost'].min())
print(sales['Unit_Cost'].max())
plt.show()
