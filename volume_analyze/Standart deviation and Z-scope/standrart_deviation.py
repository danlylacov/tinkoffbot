import sqlite3
import asyncio

class StandartDeviation(object):

    def __init__(self, figis: list):
        self.figis = figis
        self.historical_data_bd = sqlite3.connect('stocks.db')
        self.cur = self.historical_data_bd.cursor()


    def get_avarage_of_action_volume(self, figi): # str -> float
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


    def get_sorted_volumes(self): # -> list
        '''
        Функция получения списка средних значений объема по акциям передаваемым, как аргумент класса
        :return: список, имеющий структуру: [ [figi акции, среднее зн-е], [..], [..] ]
        '''
        result = []
        for figi in self.figis:
            result.append([figi, self.get_avarage_of_action_volume(figi)])
        return result







a = StandartDeviation(['BBG000BX7DH0', 'BBG000DBD6F6'])
print(a.get_sorted_volumes())





