import numpy as np
import pandas as pd

class Portfolio:
    coin = None
    amount = None
    value = None
    total_return = None

def getAmount(data):
    amount = np.sum(data[:, 0]) - np.sum(data[:, 2])
    return amount

def getPortfolioDetails(name, coin):
    portfolio = Portfolio()
    data = pd.read_csv('D:/Project/Crypto App/cryptoapp_1.0/cryptoapp/api/portfolio/portfolio_data/' + name + '/' + coin + '.csv')
    data = pd.DataFrame(data).to_numpy()
    portfolio.amount = getAmount(data)
    return portfolio

