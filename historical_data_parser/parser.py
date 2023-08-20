from dotenv.main import load_dotenv
import os

from datetime import timedelta
import time
from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now


load_dotenv()
TOKEN = os.environ['TINKOFF_API_TOKEN'] # токен TinkoffAPI


def get_candels(figi: str, file_name: str):# str, str -> .txt
    f'''
    функция получения свечей акции интервалом 5 мин за 60 последних дней по figi
    :param figi: figi-номер акции по которой необходимо получение данных
    :param file_name: название файла .txt в который необходимо записать данные
    :return: file_name.txt
    '''
    result = open(f'{file_name}.txt', 'w+')
    with Client(TOKEN) as client:
        for candle in client.get_all_candles(
            figi=figi,
            from_=now() - timedelta(days=60),
            interval=CandleInterval.CANDLE_INTERVAL_5_MIN,
        ):
            result.write(f'{str(candle)}\n')
            time.sleep(0.1)
    result.close()
    return result

def main(): # None -> None
    '''
    Функция записи данных о свечах (интервал 5 мин, за последние 2 месяца) по акциям из файла figi.txt
    Выводит:
        {figi} успешно записан! - при успешной записи данных по инструменту
        {figi} не записан! - при ошибке
    :return: None
    '''
    figis = open('figi.txt', 'r', encoding='utf-8').readlines()
    for i in range(len(figis)):
        try:
            get_candels(str(figis[i]).split()[0], str(figis[i]).split()[0])
            print(f'{str(figis[i]).split()[1]} успешно записан!')
        except:
            print(f'{str(figis[i]).split()[1]} не записан!')

if __name__ == '__main__':
    main()



