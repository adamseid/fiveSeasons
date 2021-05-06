import pandas as pd
import numpy as np
import requests
import datetime

#CLASS DEFINITION
class Ledger:
    txid = None #array
    refid = None #array
    date = None #array
    time = None #array
    type = None #array
    asset = None #array
    amount = None #array
    balance = None #array

class CoinData:
    symbol = None #string
    txid = None #array
    refid = None #array
    unix = None #array
    date = None #array
    time = None #array
    type = None #string
    amount = None #array 
    balance = None #array

class CoinInfo:
    symbol = None #string
    balance = None #float
    balance_history = None #matrix
    purchase_value = None #float
    current_value = None #float
    returns = None #float
    gains = None #float


class CashInfo:
    symbol = None #string
    balance = None #float

class PortfolioInfo:
    cash = None #object
    bitcoin = None #object
    cardano = None #object
    dogecoin = None #object
    ethereum = None #object
    ripple = None #object
    purchase_value = None #float
    current_value = None #float
    gains = None #float
    returns = None #float


# Creates a Ledger Object based on an csv file
# Param: none
# Return: A Ledger object which holds data on data, time, type, asset, amount, and balance
def readLedger():
    filename = 'C:/Users/ethio/VS/React/cryptoapp/api/functions/excel.csv'
    data = pd.DataFrame(pd.read_csv(filename))
    ledger = Ledger()
    ledger.txid = data['txid']
    ledger.refid = data['refid']
    ledger.date = data['date']
    ledger.time = data['time']
    ledger.type = data['type']
    ledger.asset = data['asset']
    ledger.amount = data['amount']
    ledger.balance = data['balance']
    return ledger

# Creates a coin object which contains the date, time, symbol, type, amount, balance
# Param: ledger object, coin symbol, type (withdraw, fee, or trade)
# Return: A coin object of all dates, time, and balance for the coin symbol and type
def getCoinData(ledger, symbol, type):
    coin_data = CoinData()
    coin_data.symbol = symbol
    coin_data.type = type
    coin_data.date, coin_data.time, coin_data.txid, coin_data.refid, coin_data.amount, coin_data.balance = [], [], [], [], [], []
    for i in range(len(ledger.asset)):
        if ledger.asset[i] == symbol and ledger.type[i]==type:
            coin_data.txid.append(ledger.txid[i])
            coin_data.refid.append(ledger.refid[i])
            coin_data.date.append(ledger.date[i])
            coin_data.time.append(ledger.time[i])
            coin_data.amount.append(ledger.amount[i])
            coin_data.balance.append(ledger.balance[i])
    coin_data.unix = getUnix(coin_data.date)
    return coin_data

# Finds coin_info (current value of coin and its returns)
# Param: cash_trade (Total CAD used in Trades), coin_trade (Total coin used in Trades), coin_fee (Total coin used in Fee) 
#        coin_withdrawal (Total CAD used in withdrawal)
# Return: coin_info
def getCoinInfo(cash_trade, coin_trade, coin_fee):
    coin_info = CoinInfo()
    coin_info.symbol = coin_trade.symbol
    coin_info.id = getCoinID(coin_info.symbol)
    coin_info.balance = coin_fee.balance[0]
    coin_info.balance_history = getBalanceHistory(coin_fee)
    coin_info.purchase_value = getPurchaseValue(cash_trade, coin_trade)
    coin_info.current_value = getCurrentValue(coin_info)
    coin_info.gains = coin_info.current_value - coin_info.purchase_value
    coin_info.returns = coin_info.gains/coin_info.purchase_value * 100
    return coin_info

#get information on cash position
def getCashInfo(cash_trade, cash_deposit):
    cash_info = CashInfo()
    cash_info.symbol = 'CAD'
    cash_info.balance = getCashBalance(cash_trade, cash_deposit)
    return cash_info

def getPortfolioInfo(bitcoin_info, cardano_info, dogecoin_info, ethereum_info, ripple_info, datetime):
    portfolio_info = PortfolioInfo()
    portfolio_info.bitcoin = bitcoin_info
    portfolio_info.cardano = cardano_info
    portfolio_info.dogecoin = dogecoin_info
    portfolio_info.ethereum = ethereum_info
    portfolio_info.ripple = ripple_info
    portfolio_info.purchase_value = getPortfolioPurchaseValue(portfolio_info, datetime)
    return portfolio_info


#SECONDARY FUNCTIONS
#Takes coin symbol and return the id. ex: getCoinID(BTC) = 'bitcoin'
def getUnix(date):
    unix = []
    for i in range(len(date)):
        year, month, day = date[i].split('-')
        unix.append(datetime.datetime(int(year), int(month), int(day), 0, 0).timestamp())
    return unix

# A function finding the coin id.
# Param: coin symbol
# Return: The coin id
def getCoinID(symbol):
    if symbol == 'BTC':
        id = 'bitcoin'
    if symbol == 'ADA':
        id = 'cardano'
    if symbol == 'DOGE':
        id = 'dogecoin'
    if symbol == 'ETH':
        id = 'ethereum'
    if symbol == 'XRP':
        id = 'ripple'
    return id

# Finds the total amount of CAD spent to purchase a coin
# Param: cash_trade (Total CAD used in Trades), coin_trade (Total coin used in Trades), coin_withdrawal (Total CAD used in withdrawal)
# Return: A coin object of all dates, time, and balance for the coin symbol and type
def getPurchaseValue(cash_trade, coin_trade):
    index = []
    for i in range(len(coin_trade.refid)):
        for j in range(len(cash_trade.refid)):
            if coin_trade.refid[i] == cash_trade.refid[j]:
                index.append(j)
    purchase_value = 0
    for i in range(len(index)):
        purchase_value = purchase_value - cash_trade.amount[index[i]]
    return purchase_value

# Finds the current value of a coin
# Param: coin_info
# Return: The current value of a coin
def getCurrentValue(coin_info):
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=' + coin_info.id + '&vs_currencies=cad&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true').json()
    current_price = response[coin_info.id]['cad']
    current_value = coin_info.balance*current_price
    return current_value

#get current cash balance of the portfolio
def getCashBalance(cash_trade, cash_deposit):
    if cash_trade.txid[0] >= cash_deposit.txid[0]:
        balance = cash_trade.balance[0]
    else:
        balance = cash_deposit.balance[0]
    return balance


def getPortfolioPurchaseValue(portfolio_info, date):
    unix = getUnix([date])[0] #float
    balance = [portfolio_info.bitcoin.balance_history, portfolio_info.cardano.balance_history, portfolio_info.dogecoin.balance_history, portfolio_info.ethereum.balance_history, portfolio_info.ripple.balance_history]
    purchase_balance = []
    for i in range(len(balance)):
        difference = []
        for j in range(len(balance[i][0])):
            difference.append(abs(unix - balance[i][0][j]))
        index = difference.index(min(difference))
        purchase_balance.append(balance[i][2][index])
    print(purchase_balance)
    return 0

#get matrix
def getBalanceHistory(coin_fee):
    txid, unix, datetime, balance = [], [], [], []
    for i in range(len(coin_fee.txid)):
        txid.append(coin_fee.txid[i])
    txid = np.sort(txid)
    for i in range(len(txid)):
        for j in range(len(coin_fee.txid)):
            if txid[i] == coin_fee.txid[j]:
                unix.append(coin_fee.unix[j])
                datetime.append(coin_fee.date[j] + coin_fee.time[j])
                balance.append(coin_fee.balance[j])
    balance_history = [unix, datetime, balance]
    return balance_history









ledger = readLedger()

cash_trade = getCoinData(ledger, 'CAD', 'Trade')
cash_deposit = getCoinData(ledger, 'CAD', 'Deposit')
cash_info = getCashInfo(cash_trade, cash_deposit)

bitcoin_trade = getCoinData(ledger, 'BTC', 'Trade')
bitcoin_fee = getCoinData(ledger, 'BTC', 'Fee')
bitcoin_info = getCoinInfo(cash_trade, bitcoin_trade, bitcoin_fee)

cardano_trade = getCoinData(ledger, 'ADA', 'Trade')
cardano_fee = getCoinData(ledger, 'ADA', 'Fee')
cardano_info = getCoinInfo(cash_trade, cardano_trade, cardano_fee)

dogecoin_trade = getCoinData(ledger, 'DOGE', 'Trade')
dogecoin_fee = getCoinData(ledger, 'DOGE', 'Fee')
dogecoin_info = getCoinInfo(cash_trade, dogecoin_trade, dogecoin_fee)

ethereum_trade = getCoinData(ledger, 'ETH', 'Trade')
ethereum_fee = getCoinData(ledger, 'ETH', 'Fee')
ethereum_info = getCoinInfo(cash_trade, ethereum_trade, ethereum_fee)

ripple_trade = getCoinData(ledger, 'XRP', 'Trade')
ripple_fee = getCoinData(ledger, 'XRP', 'Fee')
ripple_info = getCoinInfo(cash_trade, ripple_trade, ripple_fee)

coin_data = [[bitcoin_trade, bitcoin_fee], [cardano_trade, cardano_fee], [dogecoin_trade, dogecoin_fee], [ethereum_trade, ethereum_fee], [ripple_trade, ripple_fee]]
coin_info = [bitcoin_info, cardano_info, dogecoin_info, ethereum_info, ripple_info]



print(cash_info.__dict__)
print(bitcoin_info.__dict__)
print(cardano_info.__dict__)
print(dogecoin_info.__dict__)
print(ethereum_info.__dict__)
print(ripple_info.__dict__)






