from dotenv.main import load_dotenv
import os
from datetime import timedelta
from tinkoff.invest import Client, CandleInterval
from tinkoff.invest.utils import now




class StreamParser(object):

    def __init__(self, figis: list, interval: int = 5):
        '''
        Конструктор класса
        :param figis: figi акций, по котромым необходимо получить свечи
        :param interval: интервал получаемых свечей в мин, default = 5
        '''
        load_dotenv()
        self.TOKEN = os.environ['TINKOFF_API_TOKEN']
        self.figis = figis
        self.interval = interval


    def parse(self, figi:str, interval:int =5): # str, int -> HistoricCandle
        '''
           функция для получения свечи по акции в данный момент

           arguments:
               figi - figi-номер акции(содержится в файле figi.txt)
               interval - интервал требуемой свечи в мин(default: 5)

           :return:
               свеча в формате - HistoricCandle(открытие, верхняя граница, нижняя граница, закрытие, объём, время, завершена(bool))

               !!!ВАЖНО: в свече указано время по часовому поясу UTC+00.00
               '''

        # установка временного интервала
        if interval == 1:
            interval_method = CandleInterval.CANDLE_INTERVAL_1_MIN
        elif interval == 5:
            interval_method = CandleInterval.CANDLE_INTERVAL_5_MIN
        elif interval == 2:
            interval_method = CandleInterval.CANDLE_INTERVAL_2_MIN
        elif interval == 3:
            interval_method = CandleInterval.CANDLE_INTERVAL_3_MIN
        elif interval == 10:
            interval_method = CandleInterval.CANDLE_INTERVAL_10_MIN
        elif interval == 15:
            interval_method = CandleInterval.CANDLE_INTERVAL_15_MIN
        elif interval == 30:
            interval_method = CandleInterval.CANDLE_INTERVAL_30_MIN
        elif interval == 60:
            interval_method = CandleInterval.CANDLE_INTERVAL_HOUR
        elif interval == 120:
            interval_method = CandleInterval.CANDLE_INTERVAL_2_HOUR
        elif interval == 1440:
            interval_method = CandleInterval.CANDLE_INTERVAL_DAY
        else:
            raise ValueError('incorrect time interval!')

        try:
            with Client(self.TOKEN) as client:  # подключение по токену
                for candle in client.get_all_candles(  # вызов метода получения свечи
                        figi=figi,
                        from_=now() - timedelta(minutes=interval),

                        interval=interval_method,
                ):
                    return candle
        except:
            print(f"GET ERROR: Can't get candle of action with Figi: {figi}!")


    def stream_parser(self): # -> dict
        '''
        функция получения свечей по figi переданным в конструктор
        :return: словарь {figi: HistoricCandle}
        '''
        result = {}
        for i in range(len(self.figis)):
            candle = self.parse(self.figis[i], self.interval)
            result[self.figis[i]] = candle
        return result



























