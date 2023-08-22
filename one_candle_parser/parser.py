from dotenv.main import load_dotenv
import os
from datetime import timedelta
from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now

figis = ['BBG004730JJ5', 'BBG004S686N0', 'BBG008F2T3T2', 'BBG000RJL816', 'BBG000VKG4R5', 'BBG004731489', 'BBG000TJ6F42', 'BBG000Q7GG57', 'BBG0029SFXB3', 'BBG004S687G6', 'BBG005D1WCQ1', 'BBG000FWGSZ5', 'BBG000N16BP3', 'BBG004S686W0', 'BBG004S68FR6', 'BBG0029SG1C1', 'BBG000NLC9Z6', 'BBG00475K2X9', 'BBG004S685M3', 'BBG006L8G4H1', 'BBG004S68614', 'BBG000BX7DH0', 'BBG004730ZJ9', 'BBG004731354', 'BBG000GQSRR5', 'BBG000RMWQD4', 'BBG000RP8V70', 'BBG00475JZZ6', 'BBG004730RP0', 'BBG000NLHR27', 'BBG002B2J5X0', 'BBG004S68696', 'BBG000K3STR7', 'BBG00475K6C3', 'BBG001M2SC01', 'BBG000KTF667', 'BBG0014PFYM2', 'BBG0047315Y7', 'BBG00VPKLPX4', 'BBG000PKWCQ7', 'BBG000Q49F45', 'BBG000QW1WH0', 'BBG004S68B31', 'BBG002458LF8', 'BBG000RTHVK7', 'BBG000W325F7', 'BBG004S687W8', 'BBG004S68829', 'BBG0047315D0', 'BBG000DBD6F6', 'BBG000QFH687', 'BBG00B8NN386', 'BBG000F6YP24', 'BBG00HY6V6H5', 'BBG00178PGX3', 'BBG00F9XX7H4', 'BBG003LYCMB1', 'BBG004S688G4', 'BBG004RVFCY3', 'BBG007N0Z367', 'BBG00F40L971', 'BBG000LNHHJ9', 'BBG000SK7JS5', 'BBG0018X6YV1', 'BBG000RK52V1', 'BBG001DJNR51', 'BBG004S682J4', 'BBG000VG1034', 'BBG004731032', 'BBG000R607Y3', 'BBG000QJW156', 'BBG004RVFFC0', 'BBG002YFXL29', 'BBG001BBSZV8', 'BBG000MZL2S9', 'BBG004S682Z6', 'BBG00QPYJ5H0', 'BBG004S68CV8', 'BBG000PZ0833', 'BBG004S68CP5', 'BBG004730N88', 'BBG002B25NL9', 'BBG004Z2RGW8', 'BBG004S68BH6', 'BBG004S689R0', 'BBG003BNWBP3', 'BBG004S681B4', 'BBG004S68JR8', 'BBG000Q7ZZY2']



load_dotenv()
TOKEN = os.environ['TINKOFF_API_TOKEN'] # токен TinkoffAPI


def get_candels(figi: str, time):# str, str -> .txt


    with Client(TOKEN) as client:
        for candle in client.get_all_candles(
            figi=figi,
            from_=now()-timedelta(seconds=int(split_time_in_sec(str(now())) - split_time_in_sec(str(time)))),
            interval=CandleInterval.CANDLE_INTERVAL_1_MIN,
        ):
            return candle
            break






def split_time_in_sec(time):
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    day_28 = [2]
    time = time.split('.')[0]
    date, time = time.split()[0], time.split()[1]
    month, day = int(date.split('-')[1]), int(date.split('-')[2])
    hour, minute, sec = int(time.split(':')[0]), int(time.split(':')[1]), int(time.split(':')[2])
    if month in day_31:
        return sec + 60*minute +  60*60*hour + 60*60*24*day + 60*60*24*31*month
    if month in day_30:
        return sec + 60 * minute + 60 * 60 * hour + 60 * 60 * 24 * day + 60 * 60 * 24 * 30 * month
    if month in day_28:
        return sec + 60 * minute + 60 * 60 * hour + 60 * 60 * 24 * day + 60 * 60 * 24 * 28 * month



# 2023-06-12 6:25

if __name__ == '__main__':
    while True:
        print(now())
        figi = str(input('Введи figi aкции: '))
        if figi not in figis:
            raise ValueError('Не правильно введён figi!')
        time = str(input('Введи время, по которой хочешь получить свечу (гг-мес-дд чч:мин:сек):'))

        try:
            print(get_candels(figi, time))
        except:
            raise ValueError('ошибка, проверь формат ввода времени!')

# 2023-08-21 14:23:13