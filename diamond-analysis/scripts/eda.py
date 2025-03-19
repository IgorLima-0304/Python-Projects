import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('diamonds.csv')

print(df.describe())

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribuição dos Preços dos Diamantes')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='cut', y='price', data=df)
plt.title('Preço dos Diamantes por Tipo de Corte')
plt.show()

correlation_matrix = df[['carat', 'price', 'x', 'y', 'z']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()