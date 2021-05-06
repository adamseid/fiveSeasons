from django.urls import path
from .views import DataView, GetResponse, SendDate, George, MemberPortfolio, FundPortfolio, CoinInfo

urlpatterns = [
    path('data', DataView.as_view()),
    path('get-response', GetResponse.as_view()),
    path('date', SendDate.as_view()),
    path('george', George.as_view()),
    path('member-portfolio', MemberPortfolio.as_view()),
    path('fund-portfolio', FundPortfolio.as_view()),
    path('coin-info', CoinInfo.as_view()),
]