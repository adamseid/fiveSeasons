from django.urls import path
from .views import index

urlpatterns = [
    path('landingpage', index),
    path('mainpage', index),
    path('test', index)
]
