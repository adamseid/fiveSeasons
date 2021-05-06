from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DataSerializer
from .models import Data
import time
from .coin_data.coin_data import getCoinData
from .portfolio.portfolio import getPortfolioDetails
from .functions import memberPortfolio, fundPortfolio, coinInfo





# Create your views here.
def main(request):
    return HttpResponse('<h1>Hello</h1>')


class DataView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class GetResponse(APIView):
    def get(self, request, format=None):
        time.sleep(2)
        return Response({'response': 'Invalid Room Code.'}, status=status.HTTP_200_OK)

class SendDate(APIView):
    def get(self, request, format=None):
        CoinData = getCoinData('BTCUSDT')
        return Response(CoinData.volume_BTC[0])

class George(APIView):
    def get(self, request, format=None):
        portfolio = getPortfolioDetails('george', 'ETH')
        return Response(portfolio.amount)

class MemberPortfolio(APIView):
    def get(self, request, format=None):
        portfolio = memberPortfolio.get('466565157')
        return Response(portfolio.time)

class FundPortfolio(APIView):
    def get(self, request, format=None):
        bitcoin = fundPortfolio.getCoinInfo('ethereum')
        #fund_info = fundPortfolio.getFundInfo()
        return Response(bitcoin_info.__dict__)

class CoinInfo(APIView):
    def get(self, request, format=None):
        ledger = coinInfo.readLedger()

        cash_trade = coinInfo.getCoinData(ledger, 'CAD', 'Trade')
        cash_deposit = coinInfo.getCoinData(ledger, 'CAD', 'Deposit')
        cash_info = coinInfo.getCashInfo(cash_trade, cash_deposit)

        bitcoin_trade = coinInfo.getCoinData(ledger, 'BTC', 'Trade')
        bitcoin_fee = coinInfo.getCoinData(ledger, 'BTC', 'Fee')
        bitcoin_info = coinInfo.getCoinInfo(cash_trade, bitcoin_trade, bitcoin_fee)

        cardano_trade = coinInfo.getCoinData(ledger, 'ADA', 'Trade')
        cardano_fee = coinInfo.getCoinData(ledger, 'ADA', 'Fee')
        cardano_info = coinInfo.getCoinInfo(cash_trade, cardano_trade, cardano_fee)

        dogecoin_trade = coinInfo.getCoinData(ledger, 'DOGE', 'Trade')
        dogecoin_fee = coinInfo.getCoinData(ledger, 'DOGE', 'Fee')
        dogecoin_info = coinInfo.getCoinInfo(cash_trade, dogecoin_trade, dogecoin_fee)

        ethereum_trade = coinInfo.getCoinData(ledger, 'ETH', 'Trade')
        ethereum_fee = coinInfo.getCoinData(ledger, 'ETH', 'Fee')
        ethereum_info = coinInfo.getCoinInfo(cash_trade, ethereum_trade, ethereum_fee)

        ripple_trade = coinInfo.getCoinData(ledger, 'XRP', 'Trade')
        ripple_fee = coinInfo.getCoinData(ledger, 'XRP', 'Fee')
        ripple_info = coinInfo.getCoinInfo(cash_trade, ripple_trade, ripple_fee)

        return Response(bitcoin_info.__dict__)