import pandas as pd
import datetime as dt
import numpy as np

class CoinData:
    unix = None
    open = None
    high = None
    low = None
    close = None
    volume_BTC = None
    volume_USDT = None
    tradecount = None


def getUnix(date):
    unix = []
    for i in range(len(date)):
        time_array = date[i]
        time_array = time_array.replace('/', ' ')
        time_array = time_array.replace(':', ' ')
        time_array = time_array.split()
        for i in range(len(time_array)):
            time_array[i] = int(time_array[i])
        unix.append(dt.datetime(time_array[2], time_array[0], time_array[1], time_array[3], time_array[4]).timestamp())
    return unix

def getCoinData(filename):
    data = pd.read_csv('D:/Project/Crypto App/cryptoapp_1.0/cryptoapp/api/coin_data/data/' + filename + '.csv')
    data = pd.DataFrame(data).to_numpy()
    data = np.delete(data, 0, axis=0)
    coin_data = CoinData()
    coin_data.unix = getUnix(data[:, 1])
    coin_data.open = data[:, 3]
    coin_data.high = data[:, 4]
    coin_data.low = data[:, 5]
    coin_data.close = data[:, 6]
    coin_data.volume_BTC = data[:, 7]
    coin_data.volume_USDT = data[:, 8]
    coin_data.tradecount = data[:, 9]
    return coin_data







