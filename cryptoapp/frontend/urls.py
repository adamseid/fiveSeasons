from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('mainpage', index),
    path('test', index)
]
