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
from .functions import memberPortfolio, fundPortfolio





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
        #bitcoin = fundPortfolio.getCoinInfo('ethereum')
        fund_info = fundPortfolio.getFundInfo()
        return Response(fund_info.__dict__)