# -*- coding: utf-8 -*-
"""Bolsa de valores

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BqK7_mxcSbfbbx02t6tWcyp_Qq7LKXua
"""

import yfinance as yf
import pandas as pd
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta

# Símbolos das ações da Petrobras em dólar e reais
simbolo_dolar = 'PETR4.SA'
simbolo_real = 'PETR3.SA'
simbolo_usd_brl = 'USDBRL=X'

# Definir o período desejado
inicio = '2020-01-01'
fim = '2023-11-01'

# Obter os dados das ações em dólar
petrobras_dolar = yf.Ticker(simbolo_dolar)
dados_dolar = petrobras_dolar.history(period="1d", start=inicio, end=fim)

# Obter os dados das ações em reais
petrobras_real = yf.Ticker(simbolo_real)
dados_real = petrobras_real.history(period="1d", start=inicio, end=fim)

# Obter a taxa de câmbio USD/BRL
taxa_cambio = yf.Ticker(simbolo_usd_brl)
dados_cambio = taxa_cambio.history(period="1d", start=inicio, end=fim)


# Salvar os DataFrames em arquivos CSV
dados_dolar.to_csv('petrobras_dolar.csv')
dados_real.to_csv('petrobras_real.csv')
dados_cambio.to_csv('taxa_cambio_usd_brl.csv')



# Imprimir os DataFrames
print("Dados em Dólar:")
print(dados_dolar)

print("Dados em Real:")
print(dados_real)

print("Taxa de Câmbio USD/BRL:")
print(dados_cambio)

# Símbolo do ETF BOVA11.SA
simbolo_bova11 = 'BOVA11.SA'

# Definir o período desejado
inicio = '2020-01-01'
fim = '2023-11-01'

# Obter os dados do ETF BOVA11.SA
bova11 = yf.Ticker(simbolo_bova11)
dados_bova11 = bova11.history(period="1d", start=inicio, end=fim)

# Salvar o DataFrame em um arquivo CSV
dados_bova11.to_csv('bova11_data.csv')

# Imprimir o DataFrame
print("Dados do ETF BOVA11.SA:")
print(dados_bova11)

# Estatísticas descritivas para PETR4.SA
print("Estatísticas descritivas para PETR4.SA:")
print(dados_dolar['Close'].describe().round(1))

# Estatísticas descritivas para PETR3.SA
print("Estatísticas descritivas para PETR3.SA:")
print(dados_real['Close'].describe().round(1))

# Estatísticas descritivas para BOVA11.SA
print("Estatísticas descritivas para BOVA11.SA:")
print(dados_bova11['Close'].describe().round(1))

# Gráfico de linhas para PETR4.SA
plt.figure(figsize=(12, 6))
plt.plot(dados_dolar.index, dados_dolar['Close'], label='PETR4.SA')
plt.plot(dados_real.index, dados_real['Close'], label='PETR3.SA')
plt.plot(dados_bova11.index, dados_bova11['Close'], label='BOVA11.SA')
plt.title('Tendência das bolsas de valores')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.legend()
plt.show()

# Calcular a variação percentual diária para cada ativo
dados_dolar['Variação Percentual Dólar'] = dados_dolar['Close'].pct_change() * 100
dados_real['Variação Percentual Real'] = dados_real['Close'].pct_change() * 100
#dados_bova11['Variação Percentual BOVA11'] = dados_bova11['Close'].pct_change() * 100

# Gráfico de barras da volatilidade
plt.figure(figsize=(12, 6))
plt.bar(dados_dolar.index, dados_dolar['Variação Percentual Dólar'], label='PETR4.SA', alpha=0.5)
plt.bar(dados_real.index, dados_real['Variação Percentual Real'], label='PETR3.SA', alpha=0.5)
#plt.bar(dados_bova11.index, dados_bova11['Variação Percentual BOVA11'], label='BOVA11.SA', alpha=0.5)
plt.title('Volatilidade de PETR4.SA ~ PETR3.SA')
plt.xlabel('Data')
plt.ylabel('Variação Percentual Diária (%)')
plt.legend()
plt.show()

# Dividindo os dados por ano
dados_dolar_2020 = dados_dolar['2020']
dados_real_2020 = dados_real['2020']

# Criando subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico para 2020
ax.bar(dados_dolar_2020.index, dados_dolar_2020['Variação Percentual Dólar'], label='PETR4.SA', alpha=0.5)
ax.bar(dados_real_2020.index, dados_real_2020['Variação Percentual Real'], label='PETR3.SA', alpha=0.5)
ax.set_title('Volatilidade de PETR4.SA ~ PETR3.SA (2020)')
ax.set_xlabel('Data')
ax.set_ylabel('Variação Percentual Diária (%)')
ax.legend()

# Exibindo o gráfico
plt.show()

# Dividindo os dados por ano
dados_dolar_2021 = dados_dolar['2021']
dados_real_2021 = dados_real['2021']

# Criando subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico para 2021
ax.bar(dados_dolar_2021.index, dados_dolar_2021['Variação Percentual Dólar'], label='PETR4.SA', alpha=0.5)
ax.bar(dados_real_2021.index, dados_real_2021['Variação Percentual Real'], label='PETR3.SA', alpha=0.5)
ax.set_title('Volatilidade de PETR4.SA ~ PETR3.SA (2021)')
ax.set_xlabel('Data')
ax.set_ylabel('Variação Percentual Diária (%)')
ax.legend()

# Exibindo o gráfico
plt.show()

# Dividindo os dados por ano
dados_dolar_2022 = dados_dolar['2022']
dados_real_2022 = dados_real['2022']

# Criando subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico para 2022
ax.bar(dados_dolar_2022.index, dados_dolar_2022['Variação Percentual Dólar'], label='PETR4.SA', alpha=0.5)
ax.bar(dados_real_2022.index, dados_real_2022['Variação Percentual Real'], label='PETR3.SA', alpha=0.5)
ax.set_title('Volatilidade de PETR4.SA ~ PETR3.SA (2022)')
ax.set_xlabel('Data')
ax.set_ylabel('Variação Percentual Diária (%)')
ax.legend()

# Exibindo o gráfico
plt.show()

# Dividindo os dados por ano
dados_dolar_2023 = dados_dolar['2023']
dados_real_2023 = dados_real['2023']

# Criando subplots
fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico para 2023
ax.bar(dados_dolar_2023.index, dados_dolar_2023['Variação Percentual Dólar'], label='PETR4.SA', alpha=0.5)
ax.bar(dados_real_2023.index, dados_real_2023['Variação Percentual Real'], label='PETR3.SA', alpha=0.5)
ax.set_title('Volatilidade de PETR4.SA ~ PETR3.SA (2023)')
ax.set_xlabel('Data')
ax.set_ylabel('Variação Percentual Diária (%)')
ax.legend()

# Exibindo o gráfico
plt.show()

# Classificar os dados por data, se ainda não estiverem classificados
dados_bova11.sort_values('Date', inplace=True)

# Dividir os dados em conjuntos de treinamento e teste (80% treinamento, 20% teste)
train_size = int(len(dados_bova11) * 0.8)
train, test = dados_bova11.iloc[:train_size], dados_bova11.iloc[train_size:]

# Criar uma função para extrair características (features) úteis
def extract_features(df):
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Day'] = df.index.day
    return df

# Extrair características para treinamento e teste
train_features = extract_features(train.copy())
test_features = extract_features(test.copy())

# Separar as características e os rótulos
X_train, y_train = train_features.drop('Close', axis=1), train['Close']
X_test, y_test = test_features.drop('Close', axis=1), test['Close']

# Treinar um modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Avaliar o desempenho do modelo
print(f'MSE (Treinamento): {mean_squared_error(y_train, train_predictions)}')
print(f'MSE (Teste): {mean_squared_error(y_test, test_predictions)}')

# Visualizar as previsões
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Close'], label='Treinamento')
plt.plot(test.index, test['Close'], label='Teste')
plt.plot(test.index, test_predictions, label='Previsões')
plt.legend()
plt.title('Previsão de Oscilações do BOVA11.SA')
plt.xlabel('Data')
plt.ylabel('Fechamento')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Certifique-se de que os dados estão ordenados por data
dados_bova11.sort_values('Date', inplace=True)

# Dividir os dados em conjuntos de treinamento e teste (80% treinamento, 20% teste)
train_size = int(len(dados_bova11) * 0.8)
train, test = dados_bova11.iloc[:train_size], dados_bova11.iloc[train_size:]

# Treinamento do modelo ARIMA
model = ARIMA(train['Close'], order=(100,0,1))
fit_model = model.fit()

# Previsões no conjunto de treinamento
train_predictions = fit_model.predict(start=1, end=len(train), typ='levels')

# Previsões no conjunto de teste
test_predictions = fit_model.predict(start=len(train), end=len(train) + len(test) - 1, typ='levels')

# Resetar o índice para garantir que os índices estejam alinhados
train = train.reset_index(drop=True)

# Avaliação do desempenho do modelo
train_predictions.index = train['Close'].index
print(f'MSE (Treinamento): {mean_squared_error(train["Close"], train_predictions)}')

test_predictions.index = test['Close'].index
print(f'MSE (Teste): {mean_squared_error(test["Close"], test_predictions)}')



# Visualizar as previsões
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Close'], label='Treinamento')
plt.plot(test.index, test['Close'], label='Teste')
plt.plot(test.index, test_predictions, label='Previsões ARIMA')
plt.legend()
plt.title('Previsão de Oscilações do BOVA11.SA usando ARIMA')
plt.xlabel('Data')
plt.ylabel('Fechamento')
plt.show()

# Classificar os dados por data, se ainda não estiverem classificados
dados_bova11.sort_values('Date', inplace=True)


# Dividir os dados em conjuntos de treinamento e teste (80% treinamento, 20% teste)
train_size = int(len(dados_bova11) * 0.8)
train, test = dados_bova11.iloc[:train_size], dados_bova11.iloc[train_size:]

# Treinar o modelo ARIMA
order = (50, 1, 1)
model = ARIMA(train['Close'], order=order)
model_fit = model.fit()

# Fazer previsões
start_date = test.index[0]
end_date = test.index[-1] + timedelta(days=1)


# Visualizar as previsões
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Close'], label='Treinamento')
plt.plot(test.index, test['Close'], label='Teste')
plt.plot(predictions.index, predictions, label='Previsões')
plt.legend()
plt.title('Previsão de Oscilações do BOVA11.SA usando ARIMA')
plt.xlabel('Data')
plt.ylabel('Fechamento')
plt.show()