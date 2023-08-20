from dotenv.main import load_dotenv
import os
import asyncio
from datetime import timedelta
from tinkoff.invest import Client, CandleInterval
from tinkoff.invest.utils import now


load_dotenv()
TOKEN = os.environ['TINKOFF_API_TOKEN'] # токен TinkoffAPI

# figi акций индекса мосбиржи
figis = ['BBG004730JJ5', 'BBG004S686N0', 'BBG008F2T3T2', 'BBG000RJL816', 'BBG000VKG4R5', 'BBG004731489', 'BBG000TJ6F42', 'BBG000Q7GG57', 'BBG0029SFXB3', 'BBG004S687G6', 'BBG005D1WCQ1', 'BBG000FWGSZ5', 'BBG000N16BP3', 'BBG004S686W0', 'BBG004S68FR6', 'BBG0029SG1C1', 'BBG000NLC9Z6', 'BBG00475K2X9', 'BBG004S685M3', 'BBG006L8G4H1', 'BBG004S68614', 'BBG000BX7DH0', 'BBG004730ZJ9', 'BBG004731354', 'BBG000GQSRR5', 'BBG000RMWQD4', 'BBG000RP8V70', 'BBG00475JZZ6', 'BBG004730RP0', 'BBG000NLHR27', 'BBG002B2J5X0', 'BBG004S68696', 'BBG000K3STR7', 'BBG00475K6C3', 'BBG001M2SC01', 'BBG000KTF667', 'BBG0014PFYM2', 'BBG0047315Y7', 'BBG00VPKLPX4', 'BBG000PKWCQ7', 'BBG000Q49F45', 'BBG000QW1WH0', 'BBG004S68B31', 'BBG002458LF8', 'BBG000RTHVK7', 'BBG000W325F7', 'BBG004S687W8', 'BBG004S68829', 'BBG0047315D0', 'BBG000DBD6F6', 'BBG000QFH687', 'BBG00B8NN386', 'BBG000F6YP24', 'BBG00HY6V6H5', 'BBG00178PGX3', 'BBG00F9XX7H4', 'BBG003LYCMB1', 'BBG004S688G4', 'BBG004RVFCY3', 'BBG007N0Z367', 'BBG00F40L971', 'BBG000LNHHJ9', 'BBG000SK7JS5', 'BBG0018X6YV1', 'BBG000RK52V1', 'BBG001DJNR51', 'BBG004S682J4', 'BBG000VG1034', 'BBG004731032', 'BBG000R607Y3', 'BBG000QJW156', 'BBG004RVFFC0', 'BBG002YFXL29', 'BBG001BBSZV8', 'BBG000MZL2S9', 'BBG004S682Z6', 'BBG00QPYJ5H0', 'BBG004S68CV8', 'BBG000PZ0833', 'BBG004S68CP5', 'BBG004730N88', 'BBG002B25NL9', 'BBG004Z2RGW8', 'BBG004S68BH6', 'BBG004S689R0', 'BBG003BNWBP3', 'BBG004S681B4', 'BBG004S68JR8', 'BBG000Q7ZZY2']



async def parse(figi:str, interval:int =5): # str, int -> HistoricCandle
    '''
    функция для получения свечи по акции

    arguments:
        figi - figi-номер акции(содержится в файле figi.txt)
        interval - интервал требуемой свечи в мин(default: 5)

    :return:
        свеча в формате - HistoricCandle(открытие, верхняя граница, нижняя граница, закрытие, объём, время, завершена(bool))
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



    with Client(TOKEN) as client:                                   # подключение по токену
        for candle in client.get_all_candles(                       # вызов метода получения свечи
            figi=figi,
            from_=now() - timedelta(minutes=interval),
            interval=interval_method,
        ):

            return candle





async def main():# None -> list
    '''
    функция ассинхронного вызова parse с записью полученных значений в список
    :return:
        список со свечами акций по индексу мосбиржи
    '''
    request = await asyncio.gather(

        # сюда вызывать функцию parse для каждого figi

        parse("BBG004730JJ5"), parse("BBG004S686N0"), parse("BBG008F2T3T2"), parse("BBG000RJL816"), parse("BBG000VKG4R5"), parse("BBG004731489"), parse("BBG000TJ6F42"), parse("BBG000Q7GG57"), parse("BBG0029SFXB3"), parse("BBG004S687G6"), parse("BBG005D1WCQ1"), parse("BBG000FWGSZ5"), parse("BBG000N16BP3"), parse("BBG004S686W0"), parse("BBG004S68FR6"), parse("BBG0029SG1C1"), parse("BBG000NLC9Z6"), parse("BBG00475K2X9"), parse("BBG004S685M3"), parse("BBG006L8G4H1"), parse("BBG004S68614"), parse("BBG000BX7DH0"), parse("BBG004730ZJ9"), parse("BBG004731354"), parse("BBG000GQSRR5"), parse("BBG000RMWQD4"), parse("BBG000RP8V70"), parse("BBG00475JZZ6"), parse("BBG004730RP0"), parse("BBG000NLHR27"), parse("BBG002B2J5X0"), parse("BBG004S68696"), parse("BBG000K3STR7"), parse("BBG00475K6C3"), parse("BBG001M2SC01"), parse("BBG000KTF667"), parse("BBG0014PFYM2"), parse("BBG0047315Y7"), parse("BBG00VPKLPX4"), parse("BBG000PKWCQ7"), parse("BBG000Q49F45"), parse("BBG000QW1WH0"), parse("BBG004S68B31"), parse("BBG002458LF8"), parse("BBG000RTHVK7"), parse("BBG000W325F7"), parse("BBG004S687W8"), parse("BBG004S68829"), parse("BBG0047315D0"), parse("BBG000DBD6F6"), parse("BBG000QFH687"), parse("BBG00B8NN386"), parse("BBG000F6YP24"), parse("BBG00HY6V6H5"), parse("BBG00178PGX3"), parse("BBG00F9XX7H4"), parse("BBG003LYCMB1"), parse("BBG004S688G4"), parse("BBG004RVFCY3"), parse("BBG007N0Z367"), parse("BBG00F40L971"), parse("BBG000LNHHJ9"), parse("BBG000SK7JS5"), parse("BBG0018X6YV1"), parse("BBG000RK52V1"), parse("BBG001DJNR51"), parse("BBG004S682J4"), parse("BBG000VG1034"), parse("BBG004731032"), parse("BBG000R607Y3"), parse("BBG000QJW156"), parse("BBG004RVFFC0"), parse("BBG002YFXL29"), parse("BBG001BBSZV8"), parse("BBG000MZL2S9"), parse("BBG004S682Z6"), parse("BBG00QPYJ5H0"), parse("BBG004S68CV8"), parse("BBG000PZ0833"), parse("BBG004S68CP5"), parse("BBG004730N88"), parse("BBG002B25NL9"), parse("BBG004Z2RGW8"), parse("BBG004S68BH6"), parse("BBG004S689R0"), parse("BBG003BNWBP3"), parse("BBG004S681B4"), parse("BBG004S68JR8"), parse("BBG000Q7ZZY2"),

    )
    print(request)


if __name__ == "__main__":
    asyncio.run(main())