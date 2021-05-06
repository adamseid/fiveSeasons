import pandas as pd

class Portfolio:
    time = None
    contribution = None
    total_contributions = None
    value = None
    returns = None
    gains = None

def get(id):
    portfolio = Portfolio()
    contribution_data = pd.DataFrame(pd.read_csv('D:/Crypto/Five Seasons Fund/member_transactions/' + id + '.csv')).to_numpy()
    portfolio.time = contribution_data[0][0]
    return portfolio


