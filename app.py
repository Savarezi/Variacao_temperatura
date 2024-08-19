import pandas as pd
df = pd.read_csv('data_sample_SP.csv', sep = ';')


colunas = [
    'TEMPERATURA DO AR - BULBO SECO. HORARIA (C)',
    'TEMPERATURA DO PONTO DE ORVALHO (C)',
    'TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C)'
]

# intervalo de linhas desejado
df_intervalo = df.loc[3:102, colunas]

#  colunas especificadas tem valores nulos
df_filtrado = df_intervalo.dropna()

print(df_filtrado)




import matplotlib.pyplot as plt



plt.figure(figsize=(12, 6))

#  cada coluna com uma linha diferente
for coluna in df_filtrado.columns:
    plt.plot(df_filtrado.index, df_filtrado[coluna], label=coluna)

# título e legendas
plt.title('Variação das Temperaturas ao Longo do Tempo')
plt.xlabel('Índice')
plt.ylabel('Temperatura (°C)')
plt.legend()

# Exibir o gráfico
plt.show()










