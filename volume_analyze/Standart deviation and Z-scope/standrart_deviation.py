import sqlite3
from stream_parser.parser import stream_parse
from math import sqrt

class StandartDeviation(object):

    def __init__(self, figis: list):
        self.figis = figis
        self.historical_data_bd = sqlite3.connect('stocks.db')
        self.cur = self.historical_data_bd.cursor()


    def get_avarage_of_action_volume(self, figi: str): # str -> float
        '''
        Функция получения среденего значения объёма после отсечения 25% самых мелких и 25% самых крупных значений по акции
        :param figi: figi-индефикатор акции
        :return: среднее зн-е объёма
        '''
        request = self.cur.execute(f'SELECT volume FROM {figi} ')
        result = []
        for el in request:
            result.append(int(el[0]))
        result.sort()
        result = result[len(result)//4:-(len(result)//4)]
        return sum(result)/len(result)


    def get_sorted_volumes(self, figis: list): # list -> list
        '''
        Функция получения списка средних значений объема по акциям указанным как список
        :return: список, имеющий структуру: [ [figi акции, среднее зн-е], [..], [..] ]
        '''
        result = []
        for figi in figis:
            result.append([figi, self.get_avarage_of_action_volume(figi)])
        return result


    def get_value_deviation(self, volumes: list, avarage_value: float):# list, float -> list
        '''
        Функция получения разницы (отклонения) между значением каждого объема и средним значением объема
        :param volumes: зн-я объёмов
        :param avarage_value: среднее зн-е объема
        :return: список с разницами
        '''
        deviations = [volume - avarage_value for volume in volumes]
        return deviations

    def get_standart_deviation(self, deviations: list): # list -> float
        '''
        Функция получения среднеквадратичного отклонения
        :param deviations: список с отклонениями
        :return: среднеквадратичное отклонение
        '''
        deviations = [deviation ** 2 for deviation in deviations]
        standart_deviation = sqrt(sum(deviations)/len(deviations))
        return standart_deviation


    def get_Z_analyize(self, X_i: float, X_av: float, standard_deviation: float): # float, float, float -> float
        '''
        Функция получения Z-преобразования по формуле Z_i =  Z_i = (X_i - X_av)/deviation
        :param X_i: значение объема, которое мы получаем в реальном времени
        :param X_av: среднее значение
        :param standart_deviation: среднеквадратическое отклонение
        :return: проценты (то есть величина, показывающая, в скольких стандратных отклонениях от среднего значения находится изучаемое значение объема).
        '''
        Z_i = (X_i - X_av)/standard_deviation
        return Z_i










a = StandartDeviation(['BBG000BX7DH0', 'BBG000DBD6F6'])
print(a.get_value_deviation([1, 2, 3], 1))








