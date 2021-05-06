import numpy as np
import pandas as pd
import requests

class CashInfo:
    id = None
    value = None

class CoinInfo:
    id = None
    total_amount = None
    purchase_value = None
    current_value = None
    returns = None
    gains = None

class FundInfo:
    id = None
    purchase_value = None
    current_value = None
    returns = None
    gains = None

#Calculate the value of a held coin at time of purchase
def getPurchaseValue(deposit, price, fee):
    purchase_value = 0
    for i in range(len(deposit)):
        purchase_value = purchase_value + deposit[i]*price[i] - fee[i]
    return purchase_value

#Calcuate value of a held coin with current market valuations
def getCurrentValue(id, total_amount):
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=' + id + '&vs_currencies=cad&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true').json()
    current_price = response[id]['cad']
    current_value = total_amount*current_price
    return current_value

#Creates coin object and generates attribute values by reading transaction data from csv
def getCoinInfo(id):
    data = pd.DataFrame(pd.read_csv('C:/Users/ethio/VS/FiveSeasonsFund/fund_transactions/' + id + '.csv'))
    data["deposit"] = data["deposit"].fillna(0)
    data["withdrawl"] = data["withdrawl"].fillna(0)
    data["price"] = data["price"].fillna(0)
    data["fee"] = data["fee"].fillna(0)
    data = data.to_numpy()
    deposit = data[:, 1]
    withdrawl = data[:, 2]
    price = data[:, 3]
    fee = data[:, 4]
    coin_info = CoinInfo()
    coin_info.id = id
    coin_info.total_amount = np.sum(deposit) - np.sum(withdrawl) - np.sum(fee)
    coin_info.purchase_value = getPurchaseValue(deposit, price, fee)
    coin_info.current_value = getCurrentValue(id, coin_info.total_amount)
    coin_info.returns = (coin_info.current_value - coin_info.purchase_value)/coin_info.purchase_value * 100
    coin_info.gains = coin_info.current_value - coin_info.purchase_value
    return coin_info

#Creates cash info object with attributes
def getCashInfo():
    data = pd.DataFrame(pd.read_csv('C:/Users/ethio/VS/FiveSeasonsFund/fund_transactions/' + 'cash' + '.csv')).to_numpy()
    cash_info = CashInfo()
    cash_info.id = 'cash'
    cash_info.value = np.sum(data[:, 1])
    return cash_info

#Create fund info object and generates attribute values as a function of coin attribute values
def getFundInfo():
    cash = getCashInfo()
    ethereum = getCoinInfo('ethereum')
    cardano = getCoinInfo('cardano')
    dogecoin = getCoinInfo('dogecoin')
    print(dogecoin.__dict__)
    fund_info = FundInfo() 
    fund_info.purchase_value = cash.value + ethereum.purchase_value + cardano.purchase_value + dogecoin.purchase_value
    fund_info.current_value = cash.value + ethereum.current_value + cardano.current_value + dogecoin.current_value
    fund_info.returns = (fund_info.current_value - fund_info.purchase_value)/fund_info.purchase_value * 100
    fund_info.gains = fund_info.current_value - fund_info.purchase_value
    return fund_info

