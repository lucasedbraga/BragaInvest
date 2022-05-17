import yfinance as yf
import aplicacoes

yf.pdr_override()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aplicacoes import *
import seaborn as sns
import datetime

# Obtendo e tratando dados

tickers = ["ABEV3.SA", "ITSA4.SA", "WEGE3.SA", "USIM5.SA", "VALE3.SA"]
#tickers = ["BTC-USD", "DOGE-USD", "ETH-USD"]
acoes = []
for tick in tickers:
    acoes.append(Ativo(tick))

carteira = []
for acao in acoes:
    carteira.append(acao.info_hist())

analise_dividendo = []
for acao in acoes:
    analise_dividendo.append(acao.MetricasDividendos())

print(analise_dividendo)

#carteira = web.get_data_yahoo(tickers, period= "5y")["Adj Close"]
#ibov = Ativo("^BVSP").info_hist() #, period = "max")["Adj Close"]

# Resultados

sns.set()
dataset = []
for ativo in carteira:
    # print(ativo)
    # dataset.append(datetime.timedelta(days=len(x)))
    ativo.plot(figsize=(18, 6), label=ativo.index[0][0])
plt.legend()
plt.show()
# max_time = max(dataset)
# horizonte = datetime.datetime.today() - max_time
# datas = []
# for dia in range(int(max_time.days)):
#     datas.append(datetime.datetime.strftime(horizonte-datetime.timedelta(days=dia), format="%d/%m/%Y"))

# # carteira normalizada
# invest_base = 10e3
# carteira_normalizada = (carteira/ carteira.iloc[0])*invest_base
# carteira_normalizada['saldo'] = carteira_normalizada.sum(axis=1)
#ibov_normalizado = (ibov/ibov.iloc[0])
#
# # plot
#
# carteira_normalizada['saldo'].plot(figsize=(18,8), label="Minha Carteira")
#ibov_normalizado.plot(label="IBOV")
#plt.legend()
#plt.show()





