from standart_deviation import StandartDeviation
from stream_parser.parser import StreamParser
import sqlite3
import time


class StandartDeviationAnalize(object):


    def __init__(self, figis: str, bd_name: str, interval: int = 1):
        '''
        Конструктор класса
        :param figis: название txt файла с записанными figi-индефикаторами акций
        :param bd_name: название бд с историческими данными
        :param interval: интервал рассматриваемых свеч в мин, default: 1
        '''
        self.figis = open(f'{figis}.txt', 'r', encoding='utf-8').readlines()
        self.interval = interval
        self.bd = sqlite3.connect(f'{bd_name}.db')
        self.cur = self.bd.cursor()


    def get_historic_data(self, figi: str): # -> list
        '''
        функция получения исторических данных по акции в виде списка
        :param figi: figi-индефикатор акции
        :return: список с историческими данными
        '''
        action_volume = []
        volumes = self.cur.execute(f'SELECT volume FROM {figi}')
        for el in volumes:
            action_volume.append(int(el[0]))
        return action_volume





    def analize(self): # -> list
        '''
        функция вычисления является ли зн-е объёма в настоящий момент аномальным
        :return: список со структурой list: [ [str: figi, bool: аномальное ли] , [..], .. ]
        '''
        result = []
        for i in range(len(self.figis)):
            figi = self.figis[i].split()[0]
            historic_data = self.get_historic_data(figi)


            stream_parser = StreamParser(figi, 1)
            stream_volume = stream_parser.parse()

            if stream_volume != None:
                standart_dev = StandartDeviation(historic_data, stream_volume , z_limit=2.8)
                result.append([figi, standart_dev.result])
            else:
                result.append([figi, None])

        return result
