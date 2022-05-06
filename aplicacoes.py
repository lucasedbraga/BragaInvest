from yahooquery import Ticker
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt


class Ativo():
    def __init__(self, cod):
        self.cod = str(cod)
        self.__acao = Ticker(self.cod)
        self.detalhes = pd.DataFrame(self.__acao.summary_detail)
        self.cotacao_atual = self.__acao.quotes[self.cod]['ask']
        self.hoje = datetime.date.today()

    @staticmethod
    # def ajusta_data(data):
        # max_time = max(dataset)
        # horizonte = datetime.datetime.today() - max_time
        # datas = []
        # for dia in range(int(max_time.days)):
        #     datas.append(datetime.datetime.strftime(horizonte-datetime.timedelta(days=dia), format="%d/%m/%Y"))

    def calculo_taxas(self):
        url = None


    def info_hist(self):
        hist_max = self.__acao.history(period='max')
        x = hist_max.index.to_frame()
        x = x.iloc[:, 1]
        x = list(x)
        print(x)

        return hist_max['close']
        # plt.plot(np.array(hist_max['close']))
        # plt.title(f'Histórico {self.cod}')
        # plt.show()

    def info_delta(self,dt, descricao):
        datas = [self.hoje - datetime.timedelta(days=dt) for x in range(dt)]
        hist = self.__acao.history(start=datas[-1], end=self.hoje)
        legenda = []
        for x in hist.index:
            datas = str(x[1])[5:10]
            legenda.append(datas)
        plt.plot(legenda, np.array(hist['open']), color='blue',label='Abertura')
        plt.plot(legenda, np.array(hist['close']), color = 'orange', label='Fechamento')
        plt.plot(legenda, np.array(hist['high']), color = 'green', label='Máximo')
        plt.plot(legenda,np.array(hist['low']), color = 'red', label='Mínimo')
        plt.legend()
        plt.title(f'{descricao}: {self.cod}')
        plt.show()

    def info_30_dias(self):
        self.info_delta(30,'Últimos 30 dias ')

    def info_7_dias(self):
        self.info_delta(7,'Últimos 7 dias')

    def MetricasDividendos(self):
        self.dividendoYield = self.detalhes[self.cod]['dividendYield']
        self.dividendofuturo = self.detalhes[self.cod]['dividendRate']
        self.payout = self.detalhes[self.cod]['payoutRatio']
        divida_liquida_sobre_patrimonio_liquido  = None
        divida_sobre_o_lucro_operacional = None

        if self.dividendoYield > 0.06:
            divYield_status = True
        else:
            divYield_status  = False

    def cotacaoxtempo(self):
        hist_max = pd.DataFrame(np.array(self.__acao.history(period='max')))
        ibov = pd.DataFrame(Ticker('^BVSP').history(period='max'))
        plt.plot(hist_max.rolling(window=90).mean())
        # plt.plot(hist_max, alpha=0.8)
        # plt.plot(hist_max.rolling(window=360).mean())
        plt.grid()
        plt.legend(['Média Móvel', 'Cotação Diária', 'Média Movel Anual'])
        plt.show()



if __name__ == '__main__':
    acao1 = Ativo('PETR4.SA')
    acao2 = Ativo('WEGE3.SA')
    acao3 = Ativo ('^BVSP')
    print(acao1.detalhes)
    acao1.cotacaoxtempo()


