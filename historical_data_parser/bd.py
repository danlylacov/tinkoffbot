import sqlite3

bd = sqlite3.connect('stocks.db') # подключение к бд
cur = bd.cursor()



def get_data(file:str, i:int):# str, int -> list
    '''
    функция для преобразования HistoricalCandle в список со значениями [открытие, верхняя граница, нижняя граница, закрытие, объём, время]
    :param file: название файла с данными о свечах
    :param i: порядковый номер HistoricalCandle в файле
    :return: список со значениями
    '''
    candle = file[i]
    candle = candle.split(',')
    return [candle[0].split('=')[2], candle[2].split('=')[2], candle[4].split('=')[2], candle[6].split('=')[2],
            candle[8].split('=')[1], f"{candle[9].split('(')[1].strip()}:{candle[10].strip()}:{candle[11].strip()}:{candle[12].strip()}:{candle[13].strip()}"]




def main():# None -> None
    '''
    Функция для записи данных о свечах из текстового файла в базу данных
    :return: None
    '''
    figis = open('figi.txt', 'r', encoding='utf-8').readlines()
    for i in range(len(figis)):
        name = figis[i].split()[0]
        file = open(f'{name}.txt', 'r').readlines()


        for i in range(len(file)):
            cur.execute(f"""  
                 CREATE TABLE IF NOT EXISTS {name}(
                 open TEXT,
                 high TEXT,
                 low TEXT,
                 close TEXT,
                 volume TEXT,
                 time TEXT);   
            """)

            cur.execute(f"""INSERT INTO {name}(open, high, low, close, volume, time) 
               VALUES(?, ?, ?, ?, ?, ?);""", get_data(file, i))
            bd.commit()



if __name__ == '__main__':
    main()
